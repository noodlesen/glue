"""Frames and other UI elements."""

from pgllib import C
from pglinit import DEFAULT_H, DEFAULT_W, pgl

class Frame():
    """Frame UI element."""

    def __init__(self, name, **kwargs):
        """."""
        self.name = name

        if kwargs.get('main', False):
            self.ul = C(0, DEFAULT_H)
            self.lr = C(DEFAULT_W, 0)
        else:
            self.ul = C(kwargs.get('ulx', 0), kwargs.get('uly', DEFAULT_H))
            self.lr = C(kwargs.get('lrx', DEFAULT_W), kwargs.get('uly', 0))

        self.pd = 0  # pixels
        self.rebuild()

    def set_padding_percents(self, p):
        self.pd = self.w * p / 100
        self.rebuild()


    def rebuild(self):
        self.ur = C(self.lr.x, self.ul.y)
        self.ll = C(self.ul.x, self.lr.y)
        self.w = self.ur.x - self.ul.x
        self.h = self.ul.y - self.ll.y
        if self.pd > 0:
            self.iul = C(self.ul.x + self.pd, self.ul.y - self.pd)
            self.iur = C(self.ur.x - self.pd, self.ur.y - self.pd)
            self.ilr = C(self.lr.x - self.pd, self.lr.y + self.pd)
            self.ill = C(self.ll.x + self.pd, self.ll.y + self.pd)
        else:
            self.iul = self.ul
            self.iur = self.ur
            self.ilr = self.lr
            self.ill = self.ll

    def split(self, drc, prc):
        """Make two frames from this one."""
        f1 = Frame(self.name + '_s1')
        f2 = Frame(self.name + '_s2')

        if drc == 'v':
            xbreak = self.iul.x + (self.ilr.x - self.iul.x) * prc / 100
            f1.ul = self.iul
            f1.lr = C(xbreak, self.ilr.y)
            f2.ul = C(xbreak, self.iul.y)
            f2.lr = self.ilr
            f1.rebuild()
            f2.rebuild()
        elif drc == 'h':
            ybreak = self.ilr.y + (self.iul.y - self.ilr.y) * (100 - prc) / 100
            f1.ul = self.iul
            f1.lr = C(self.ilr.x, ybreak)
            f2.ul = C(self.iul.x, ybreak)
            f2.lr = self.ilr
            f1.rebuild()
            f2.rebuild()

        return (f1, f2)

    def draw_itself(self):
        if self.pd == 0:
            pgl.draw_rect2d(self.ul, self.lr, w=2, c=[20, 20, 20])
        else:
            pgl.draw_rect2d(self.iul, self.ilr, w=2, c=[20, 20, 20])
