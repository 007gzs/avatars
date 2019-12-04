# encoding: utf-8
from __future__ import absolute_import, unicode_literals

from avatars.core import colors
from avatars.sprite.base import SpriteBase


class InitialsSprite(SpriteBase):
    default_options = {
        "background_colors": colors.COLORS,
        "background_color_level": 600,
        "font_size": 50,
        "chars": 1,
        "bold": False,
        "userAgent": "",
    }

    @classmethod
    def initials(cls, data):
        return data

    def sprite(self, random):
        background_color = self.random_from_dict(random, self['background_colors'])[self['background_color_level']]
        seed_initials = self.initials(random.seed.strip())[0:self['chars']]
        font_family = "-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,'Helvetica Neue',Arial,'Noto Sans',sans-serif"
        bold = 'font-weight: bold;' if self['bold'] else ''
        paths = (
          '<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" style="isolation:isolate; background: {backgroundColor}" viewBox="0 0 100 100" version="1.1">`',
          '<text x="50%" y="50%" style="line-height: 1; {bold} font-family: {fontFamily}; font-size: {fontSize}px" dy=".1em" alignment-baseline="middle" fill="#FFF" text-anchor="middle" dominant-baseline="middle">{seedInitials}</text>`',
          '</svg>',
        )
        svg = ''.join(paths)
        return svg.format(
            backgroundColor=background_color,
            bold=bold,
            fontFamily=font_family,
            fontSize=self['font_size'],
            seedInitials=seed_initials
        )
