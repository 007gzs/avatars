# encoding: utf-8
from __future__ import absolute_import, unicode_literals

from avatars.core import colors
from avatars.core.color import Color
from avatars.sprite.base import SpriteBase

from . import paths


class BotttsSprite(SpriteBase):
    default_options = {
        'primary_color_level': 600,
        'secondary_color_level': 400,
        'mouth_chance': 100,
        'sides_chance': 100,
        'texture_chance': 50,
        'top_change': 100,
        'colorful': True
    }

    @classmethod
    def group(cls, random, content, chance, x, y):
        if random.bool(chance):
            return '<g transform="translate({x}, {y})">{content}</g>'.format(content=content, x=x, y=y)
        else:
            return ''

    def sprite(self, random):
        primary_colors = random.pickone_value_from_dict(colors.COLORS)
        secondary_colors = random.pickone_value_from_dict(colors.COLORS)
        primary_color = primary_colors.get(self['primary_color_level'], list(primary_colors.values())[0])
        secondary_color = primary_colors.get(self['secondary_color_level'], list(primary_colors.values())[0])
        if not self['colorful']:
            secondary_color = secondary_colors.get(self['secondary_color_level'], list(secondary_colors.values())[0])
        eyes = random.pickone_value_from_dict(paths.EYES_PATHS)
        face = random.pickone_value_from_dict(paths.FACE_PATHS)
        mouth = random.pickone_value_from_dict(paths.MOUTH_PATHS)
        sides = random.pickone_value_from_dict(paths.SIDES_PATHS)
        texture = random.pickone_value_from_dict(paths.TEXTURE_PATHS)
        top = random.pickone_value_from_dict(paths.TOP_PATHS)
        svg_paths = [
            '<svg {svg_attr} viewBox="0 0 180 180" xmlns="http://www.w3.org/2000/svg" fill="none">',
            self.group(random, sides.format(color=Color(secondary_color)), self['sides_chance'], 0, 66),
            self.group(random, top.format(color=Color(secondary_color)), self['top_change'], 41, 0),
            self.group(random, face.format(
                color=Color(primary_color),
                texture=texture if random.bool(self['texture_chance']) else ''
            ), 100, 25, 44),
            self.group(random, mouth, self['mouth_chance'], 52, 124),
            self.group(random, eyes, 100, 38, 76),
            "</svg>"
        ]
        svg = "".join(svg_paths)
        return svg.format(svg_attr=self.svg_attr)
