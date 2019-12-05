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


def calc_hue(red, green, blue):
    r = red / 255
    g = green / 255
    b = blue / 255
    cmax = max(r, g, b)
    cmin = min(r, g, b)
    cdelta = cmax - cmin
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
    return hue, (cdelta, cmax, cmin)


def rgb2hsv(red, green, blue):
    hue, (cdelta, cmax, cmin) = calc_hue(red, green, blue)
    value = cmax
    saturation = 0 if cmax == 0 else cdelta / cmax
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


def rgb2hsl(red, green, blue):
    hue, (cdelta, cmax, cmin) = calc_hue(red, green, blue)

    lightness = (cmax + cmin) / 2
    if lightness == 0 or cmax == cmin:
        saturation = 0
    elif lightness <= 0.5:
        saturation = cdelta / (cmax + cmin)
    else:
        saturation = cdelta / (2 - (cmax + cmin))

    return hue, saturation, lightness


def hsl2rgb(hue, saturation, lightness):
    if saturation == 0:
        red = green = blue = lightness * 255
    else:
        if lightness < 0.5:
            q = lightness * (1 + saturation)
        else:
            q = lightness + saturation - (lightness * saturation)
        p = 2 * lightness - q
        hk = hue / 360
        tr = hk + 1 / 3
        tg = hk
        tb = hk - 1 / 3

        def _parse_tc(tc):
            if tc < 0:
                tc += 1
            if tc * 6 < 1:
                tc = p + (q - p) * 6 * tc
            elif tc * 2 < 1:
                tc = q
            elif tc * 3 < 2:
                tc = p + (q - p) * 6 * (2 / 3 - tc)
            else:
                tc = p
            return tc
        red = _parse_tc(tr) * 255
        green = _parse_tc(tg) * 255
        blue = _parse_tc(tb) * 255

    return int(red), int(green), int(blue)


class ColorFuncWarp(object):
    def __init__(self, color, func):
        self.color = color
        self.func = func

    def __getattr__(self, ratio):
        ratio = int(ratio)
        assert 0 <= ratio <= 100
        return self.func(self.color, ratio)


class Color(object):
    def __init__(self, color_hex=None):
        self._rgb = hex2rgb(color_hex) if color_hex else (0, 0, 0)
        self._hsv = None
        self._hsl = None

    def set_hsv(self, hue, saturation, value):
        self._hsv = (hue, saturation, value)
        self._hsl = None
        self._rgb = hsv2rgb(*self.hsv)

    def set_hsl(self, hue, saturation, lightness):
        self._hsl = (hue, saturation, lightness)
        self._hsv = None
        self._rgb = hsl2rgb(*self.hsl)

    def set_rgb(self, red, green, blue):
        self._rgb = (red, green, blue)
        self._hsv = None
        self._hsl = None

    def clone(self):
        c = Color()
        c._rgb = self._rgb
        c._hsv = self._hsv
        c._hsl = self._hsl
        return c

    @property
    def hex(self):
        return rgb2hex(*self._rgb)

    @property
    def hsv(self):
        if self._hsv is None:
            self._hsv = rgb2hsv(*self._rgb)
        return self._hsv

    @property
    def hsl(self):
        if self._hsl is None:
            self._hsl = rgb2hsl(*self._rgb)
        return self._hsl

    def __str__(self):
        return self.hex

    @property
    def lighten(self):
        return ColorFuncWarp(self.clone(), Color.lighten_than)

    @property
    def darken(self):
        return ColorFuncWarp(self.clone(), Color.darken_than)

    def lighten_than(self, ratio):
        ratio = ratio / 100
        hue, saturation, lightness = self.hsl
        self.set_hsl(hue, saturation, lightness * (1 + ratio))
        return self

    def darken_than(self, ratio):
        ratio = ratio / 100
        hue, saturation, lightness = self.hsl
        self.set_hsl(hue, saturation, lightness * (1 - ratio))
        return self

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
