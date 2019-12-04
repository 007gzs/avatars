# encoding: utf-8
from __future__ import absolute_import, unicode_literals

import unittest

from avatars.core.color import Color


class ColorTestCase(unittest.TestCase):

    def test_hex_converter(self):
        color = Color("#ff0000")
        self.assertEqual(color.hex, "#ff0000")
        self.assertEqual(color.hsv, (0, 1, 1))
        color = Color("#ffff00")
        self.assertEqual(color.hex, "#ffff00")
        self.assertEqual(color.hsv, (60, 1, 1))
        color = Color("#00ff00")
        self.assertEqual(color.hex, "#00ff00")
        self.assertEqual(color.hsv, (120, 1, 1))
        color = Color("#00ffff")
        self.assertEqual(color.hex, "#00ffff")
        self.assertEqual(color.hsv, (180, 1, 1))
        color = Color("#0000ff")
        self.assertEqual(color.hex, "#0000ff")
        self.assertEqual(color.hsv, (240, 1, 1))
        color = Color("#ff00ff")
        self.assertEqual(color.hex, "#ff00ff")
        self.assertEqual(color.hsv, (300, 1, 1))
        color = Color("#ffffff")
        self.assertEqual(color.hex, "#ffffff")
        self.assertEqual(color.hsv, (0, 0, 1))
        color = Color("#000000")
        self.assertEqual(color.hex, "#000000")
        self.assertEqual(color.hsv, (0, 0, 0))

    def test_brighter1(self):
        color1 = Color("#556677")
        color2 = Color("#667788")
        self.assertEqual(color1.brighter_than(color2, 25).hex, "#8eabc7")

    def test_brighter2(self):
        color1 = Color("#667788")
        color2 = Color("#556677")
        self.assertEqual(color1.brighter_than(color2, 25).hex, "#899fb6")

    def test_darker1(self):
        color1 = Color("#556677")
        color2 = Color("#667788")
        self.assertEqual(color1.darker_than(color2, 25).hex, "#333d48")

    def test_darker2(self):
        color1 = Color("#667788")
        color2 = Color("#556677")
        self.assertEqual(color1.darker_than(color2, 25).hex, "#293037")

    def test_brighter_or_darker1(self):
        color1 = Color("#556677")
        color2 = Color("#667788")
        self.assertEqual(color1.brighter_or_darker_than(color2, 25).hex, "#333d48")

    def test_brighter_or_darker2(self):
        color1 = Color("#667788")
        color2 = Color("#556677")
        self.assertEqual(color1.brighter_or_darker_than(color2, 25).hex, "#899fb6")
