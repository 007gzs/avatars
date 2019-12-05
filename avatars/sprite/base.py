# encoding: utf-8
from __future__ import absolute_import, unicode_literals


from avatars.core.seedrandom import SeedRandom


class SpriteBase(object):
    default_options = None

    def __init__(self, **options):
        self.width = options.get('width', None)
        self.height = options.get('height', self.width)
        attrs = []
        if self.width:
            attrs.append('width="%s"' % self.width)
        if self.height:
            attrs.append('height="%s"' % self.width)
        self.svg_attr = ' '.join(attrs)
        self.options = dict()
        if self.default_options and isinstance(self.default_options, dict):
            self.options.update(self.default_options)
        self.options.update(options)

    def __getitem__(self, item):
        return self.options[item]

    def create(self, seed):
        return self.sprite(SeedRandom(seed))

    def sprite(self, random):
        raise NotImplementedError
