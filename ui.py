class Frame():

    def __init__(self, name, **kwargs):

        self.name = name

        if kwargs.get('main', False):
            self.ul = C(0, H)
            self.lr = C(W, 0)


    def split(self, drc, prc):
        f1 = Frame(self.name+'_s1')
        f2 = Frame(self.name+'_s2')

        if drc == 'v':
            xbreak = self.ul.x+(self.lr.x-self.ul.x)*prc/100
            f1.ul = self.ul
            f1.lr = C(xbreak, self.lr.y)
            f2.ul = C(xbreak, self.ul.y)
            f2.lr = self.lr
        elif drc == 'h':
            ybreak = self.lr.y+(self.ul.y-self.lr.y)*(1-prc)/100
            f1.ul = self.ul
            f1.lr = C(self.lr.x, ybreak)
            f2.ul = C(self.ul.x, ybreak)
            f2.lr = self.lr

        return (f1, f2)