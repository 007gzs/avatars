# encoding: utf-8
from __future__ import absolute_import, unicode_literals, division


def hex2rgb(s):
    assert s[0] == '#'
    s = s[1:]
    if len(s) == 3:
        s = "".join([s[0], s[0], s[1], s[1], s[2], s[2]])
    assert len(s) == 6
    c = int(s, 16)
    return c // 65536, c // 256 % 256, c % 256


def rgb2hex(red, green, blue):
    return "#%06x" % (red * 65536 + green * 256 + blue)


def rgb2hsv(red, green, blue):
    r = red / 255
    g = green / 255
    b = blue / 255
    cmax = max(r, g, b)
    cmin = min(r, g, b)
    cdelta = cmax - cmin
    value = cmax
    saturation = 0 if cmax == 0 else cdelta / cmax
    hue = 0
    if cmax != cmin:
        if cmax == r:
            hue = (g - b) / cdelta
            if g < b:
                hue += 6
        elif cmax == g:
            hue = (b - r) / cdelta + 2
        elif cmax == b:
            hue = (r - g) / cdelta + 4
        hue *= 60
    return hue, saturation, value


def hsv2rgb(hue, saturation, value):
    h = hue / 60
    hi = int(h) % 6
    f = h - hi
    v = value * 255
    p = int(v * (1 - saturation))
    q = int(v * (1 - f * saturation))
    t = int(v * (1 - (1 - f) * saturation))
    v = int(v)
    if hi == 0:
        return v, t, p
    elif hi == 1:
        return q, v, p
    elif hi == 2:
        return p, v, t
    elif hi == 3:
        return p, q, v
    elif hi == 4:
        return t, p, v
    elif hi == 5:
        return v, p, q


class Color(object):
    def __init__(self, color_hex=None):
        self._rgb = hex2rgb(color_hex) if color_hex else (0, 0, 0)
        self._hsv = None

    def set_hsv(self, hue, saturation, value):
        self._hsv = (hue, saturation, value)
        self._rgb = hsv2rgb(*self.hsv)

    def set_rgb(self, red, green, blue):
        self._rgb = (red, green, blue)
        self._hsv = None

    def clone(self):
        c = Color()
        c._rgb = self._rgb
        c._hsv = self._hsv
        return c

    @property
    def hex(self):
        return rgb2hex(*self._rgb)

    @property
    def hsv(self):
        if self._hsv is None:
            self._hsv = rgb2hsv(*self._rgb)
        return self._hsv

    def brighter_than(self, color, difference):
        difference = difference / 100
        primary_h, primary_s, primary_v = self.hsv
        secondary_h, secondary_s, secondary_v = color.hsv
        if primary_v >= secondary_v + difference:
            return self
        primary_v = secondary_v + difference
        if primary_v > 1:
            primary_v = 1
        self.set_hsv(primary_h, primary_s, primary_v)
        return self

    def darker_than(self, color, difference):
        difference = difference / 100
        primary_h, primary_s, primary_v = self.hsv
        secondary_h, secondary_s, secondary_v = color.hsv
        if primary_v <= secondary_v - difference:
            return self
        primary_v = secondary_v - difference
        if primary_v < 0:
            primary_v = 0
        self.set_hsv(primary_h, primary_s, primary_v)
        return self

    def brighter_or_darker_than(self, color, difference):

        primary_h, primary_s, primary_v = self.hsv
        secondary_h, secondary_s, secondary_v = color.hsv
        if primary_v <= secondary_v:
            return self.darker_than(color, difference)
        else:
            return self.brighter_than(color, difference)


if __name__ == '__main__':
    colors = (
        ((255, 0, 0), (0, 1, 1)),
        ((255, 255, 0), (60, 1, 1)),
        ((0, 255, 0), (120, 1, 1)),
        ((0, 255, 255), (180, 1, 1)),
        ((0, 0, 255), (240, 1, 1)),
        ((255, 0, 255), (300, 1, 1)),

        ((127, 0, 0), (0, 1, 0.5)),
        ((127, 127, 0), (60, 1, 0.5)),
        ((0, 127, 0), (120, 1, 0.5)),
        ((0, 127, 127), (180, 1, 0.5)),
        ((0, 0, 127), (240, 1, 0.5)),
        ((127, 0, 127), (300, 1, 0.5)),

        ((255, 255, 255), (0, 0, 1)),
        ((192, 192, 192), (0, 0, 0.75)),
        ((127, 127, 127), (0, 0, 0.5)),
        ((0, 0, 0), (0, 0, 0)),
    )

    def _cmp(x, y):
        assert len(x) == len(y)
        for a, b in zip(x, y):
            assert abs(a - b) < 0.00001
    print(hex2rgb("#ccc"))
    for rgb, hsv in colors:
        print(rgb, rgb2hex(*rgb))
        # _cmp(hsv2rgb(*hsv), rgb)
        # _cmp(rgb2hsv(*rgb), hsv)
