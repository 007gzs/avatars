# encoding: utf-8
from __future__ import absolute_import, unicode_literals

from avatars.core.color import Color
from avatars.sprite.base import SpriteBase

from . import colors, paths


class AvatioSpriteBase(SpriteBase):
    use_paths = paths.BasePath()

    def get_color(self, random, flag):
        if flag == 'head_shape':
            return random.pickone_value_from_dict(colors.SKIN_COLORS)
        elif flag == 'eyes':
            return random.pickone_value_from_dict(colors.EYES_COLOR)
        elif flag == 'hair':
            return random.pickone_value_from_dict(colors.HAIR_COLOR)
        elif flag == 'glasses':
            return random.pickone_value_from_dict(colors.COLORS)
        elif flag == 'clothes':
            return random.pickone_value_from_dict(colors.COLORS)
        elif flag == 'clothes_secondary':
            return random.pickone_value_from_dict(colors.COLORS)
        elif flag == 'accessory':
            return random.pickone_value_from_dict(colors.COLORS)
        elif flag == 'nose':
            return random.pickone_value_from_dict(colors.LIP_COLOR)
        else:
            raise

    def sprite(self, random):
        svg_paths = [
            '<svg {svg_attr} version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 142.841 137.643">',
            self.use_paths.get_head_shape(random, color=Color(self.get_color(random, 'head_shape'))),
            self.use_paths.get_eyes(random, color=Color(self.get_color(random, 'eyes'))),
            self.use_paths.get_hair(random, color=Color(self.get_color(random, 'hair'))),
            self.use_paths.get_glasses(random, color=Color(self.get_color(random, 'glasses'))),
            self.use_paths.get_clothes(random, color=Color(self.get_color(random, 'clothes')),
                                       secondaryColor=Color(self.get_color(random, 'clothes_secondary'))),
            self.use_paths.get_accessory(random, color=Color(self.get_color(random, 'accessory'))),
            self.use_paths.get_facial_hair(random, color=Color(self.get_color(random, 'hair'))),
            self.use_paths.get_nose(random, color=Color(self.get_color(random, 'nose'))),
            '</svg>'
        ]
        svg = "".join(svg_paths)
        return svg.format(svg_attr=self.svg_attr)


class AvatioMaleSprite(AvatioSpriteBase):
    use_paths = paths.MalePath()

    def get_color(self, random, flag):
        if flag == 'mouth':
            return random.pickone_value_from_dict(colors.LIPSTICKS_COLORS)
        else:
            return super(AvatioMaleSprite, self).get_color(random, flag)


class AvatioFemaleSprite(AvatioSpriteBase):
    use_paths = paths.FemalePath()

    def get_color(self, random, flag):
        if flag == 'mouth':
            return random.pickone_value_from_dict(colors.LIP_COLOR)
        else:
            return super(AvatioFemaleSprite, self).get_color(random, flag)


class AvatioSprite(SpriteBase):
    def sprite(self, random):
        if random.bool(50):
            return AvatioMaleSprite(**self.options).sprite(random)
        else:
            return AvatioFemaleSprite(**self.options).sprite(random)
