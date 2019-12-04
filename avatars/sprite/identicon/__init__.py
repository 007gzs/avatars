# encoding: utf-8
from __future__ import absolute_import, unicode_literals

from avatars.core import colors
from avatars.sprite.base import SpriteBase


class IdenticonSprite(SpriteBase):
    default_options = {
        "padding": 0,
        "background": "#FFF",
        "color_level": 600
    }
    rows = (
        (
            '<path d="M0 4h1v1H0V4zm4 0h1v1H4V4z" fill-rule="evenodd" fill="{color}"/>',
            '<path d="M0 4h2v1H0V4zm3 0h2v1H3V4z" fill-rule="evenodd" fill="{color}"/>',
            '<path d="M0 4h5v1H0V4z" fill="{color}"/>',
            '<path d="M2 4h1v1H2V4z" fill="{color}"/>',
            '<path d="M1 4h3v1H1V4z" fill="{color}"/>',
            '<path d="M0 4h1v1H0V4zm2 0h1v1H2V4zm2 0h1v1H4V4z" fill-rule="evenodd" fill="{color}"/>',
        ),
        (
            '<path d="M0 3h1v1H0V3zm4 0h1v1H4V3z" fill-rule="evenodd" fill="{color}"/>',
            '<path d="M0 3h2v1H0V3zm3 0h2v1H3V3z" fill-rule="evenodd" fill="{color}"/>',
            '<path d="M0 3h5v1H0V3z" fill="{color}"/>',
            '<path d="M2 3h1v1H2V3z" fill="{color}"/>',
            '<path d="M1 3h3v1H1V3z" fill="{color}"/>',
            '<path d="M0 3h1v1H0V3zm2 0h1v1H2V3zm2 0h1v1H4V3z" fill-rule="evenodd" fill="{color}"/>'
        ),
        (
            '<path d="M0 2h1v1H0V2zm4 0h1v1H4V2z" fill-rule="evenodd" fill="{color}"/>',
            '<path d="M0 2h2v1H0V2zm3 0h2v1H3V2z" fill-rule="evenodd" fill="{color}"/>',
            '<path d="M0 2h5v1H0V2z" fill="{color}"/>',
            '<path d="M2 2h1v1H2V2z" fill="{color}"/>',
            '<path d="M1 2h3v1H1V2z" fill="{color}"/>',
            '<path d="M0 2h1v1H0V2zm2 0h1v1H2V2zm2 0h1v1H4V2z" fill-rule="evenodd" fill="{color}"/>',
        ),
        (
            '<path d="M0 1h1v1H0V1zm4 0h1v1H4V1z" fill-rule="evenodd" fill="{color}"/>',
            '<path d="M0 1h2v1H0V1zm3 0h2v1H3V1z" fill-rule="evenodd" fill="{color}"/>',
            '<path d="M0 1h5v1H0V1z" fill="{color}"/>',
            '<path d="M2 1h1v1H2V1z" fill="{color}"/>',
            '<path d="M1 1h3v1H1V1z" fill="{color}"/>',
            '<path d="M0 1h1v1H0V1zm2 0h1v1H2V1zm2 0h1v1H4V1z" fill-rule="evenodd" fill="{color}"/>',
        ),
        (
            '<path d="M0 0h1v1H0V0zm4 0h1v1H4V0z" fill-rule="evenodd" fill="{color}"/>',
            '<path d="M0 0h2v1H0V0zm3 0h2v1H3V0z" fill-rule="evenodd" fill="{color}"/>',
            '<path d="M0 0h5v1H0V0z" fill="{color}"/>',
            '<path d="M2 0h1v1H2V0z" fill="{color}"/>',
            '<path d="M1 0h3v1H1V0z" fill="{color}"/>',
            '<path d="M0 0h1v1H0V0zm2 0h1v1H2V0zm2 0h1v1H4V0z" fill-rule="evenodd" fill="{color}"/>',
        ),
    )

    def __init__(self, **options):
        super(IdenticonSprite, self).__init__(**options)
        self.colors = []
        color_level = self['color_level']
        for key in sorted(colors.COLORS.keys()):
            if not colors.COLORS[key]:
                continue
            self.colors.append(colors.COLORS[key].get(color_level, list(colors.COLORS[key].values())[0]))

    def sprite(self, random):
        color = random.pickone(self.colors)
        offset = 0 - self['padding']
        size = 5 + self['padding'] * 2
        paths = [
            '<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" style="isolation:isolate" viewBox="{offset} {offset} {size} {size}" version="1.1" shape-rendering="crispEdges">',
            '<path d="M{offset} {offset}h{size}v{size}H{offset}V0z" fill="{background}" />',
        ]
        for row in self.rows:
            paths.append(random.pickone(row))
        paths.append("</svg>")
        svg = "".join(paths)
        return svg.format(color=color, background=self['background'], offset=offset, size=size)
