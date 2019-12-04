# encoding: utf-8
from __future__ import absolute_import, unicode_literals

from avatars.sprite import *


def test(name, flag, sprite):
    with open("%s.svg" % flag, 'wb') as f:
        f.write(sprite().create(name).encode("utf8"))


if __name__ == '__main__':
    test("张三", "male_1", MaleSprite)
    test("张三", "female_1", FemaleSprite)
    test("张三", "identicon_1", IdenticonSprite)
    test("张三", "bottts_1", BotttsSprite)
    test("张三", "initials_1", InitialsSprite)
    test("李四", "male_2", MaleSprite)
    test("李四", "female_2", FemaleSprite)
    test("李四", "identicon_2", IdenticonSprite)
    test("李四", "bottts_2", BotttsSprite)
    test("李四", "initials_2", InitialsSprite)
