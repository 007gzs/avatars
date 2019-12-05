# encoding: utf-8
from __future__ import absolute_import, unicode_literals

from avatars.sprite import *


def test(name, flag, sprite):
    with open("%s.svg" % flag, 'wb') as f:
        f.write(sprite(width=64).create(name).encode("utf8"))


if __name__ == '__main__':
    sprites = {
        "male": MaleSprite,
        "female": FemaleSprite,
        "identicon": IdenticonSprite,
        "bottts": BotttsSprite,
        "initials": InitialsSprite,
        "gridy": GridySprite,
        "avatio_female": AvatioFemaleSprite,
        "avatio_male": AvatioMaleSprite,
    }
    names = ["张三", "李四", "王五"]
    for i, name in enumerate(names):
        for flag, sprite in sprites.items():
            file_name = "%s_%d.svg" % (flag, i)
            with open(file_name, 'wb') as f:
                f.write(sprite(width=64).create(name).encode("utf8"))
            print("""
.. image:: https://github.com/007gzs/avatars/raw/master/resource/{0}?sanitize=true
    :target: https://github.com/007gzs/avatars/raw/master/resource/{0}""".format(file_name), end='')
        print("\n\n----\n", end='')
