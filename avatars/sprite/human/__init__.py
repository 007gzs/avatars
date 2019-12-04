# encoding: utf-8
from __future__ import absolute_import, unicode_literals

from avatars.sprite.base import SpriteBase
from avatars.sprite.male import MaleSprite
from avatars.sprite.female import FemaleSprite


class HumanSprite(SpriteBase):
    default_options = {
        "mood": ('happy', 'sad', 'surprised')
    }

    def sprite(self, random):
        if random.bool(50):
            return MaleSprite(**self.options).sprite(random)
        else:
            return FemaleSprite(**self.options).sprite(random)
