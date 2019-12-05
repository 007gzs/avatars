# encoding: utf-8
from __future__ import absolute_import, unicode_literals

import random


class SeedRandom(object):
    def __init__(self, seed):
        self.seed = seed
        self.random = random.Random(seed)

    def bool(self, likelihood=50):
        return self.random.random() * 100 < likelihood

    def integer(self, min_value, max_value):
        return self.random.randrange(min_value, max_value)

    def pickone(self, arr):
        return arr[self.integer(0, len(arr))]

    def pickone_value_from_dict(self, data):
        return data[self.pickone(sorted(data.keys()))]
