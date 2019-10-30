import pyglet
from random import randint

W = 1400
H = 800

AUTO_LOOP = False

window = pyglet.window.Window(W,H)
batch = pyglet.graphics.Batch()

frames = []
bricks = []

class C():

    def init(self, x, y, z=None):
        self.x = x
        self.y = y
        self.z = z

    def v2(self):
        return (
            (self.x, self.y,)
        ) 

    def v3(self):
            return (
                (self.x, self.y, self.z)
            )

class Pgl():

    def __init__(batch):
        self.batch = batch

    def line2d(p1, p2, **kwargs):
        w = kwargs.get('w', 0)
        if w > 0:
            pyglet.gl.glLineWidth(w)

        c = kwargs.get('c', None)
        if c is not None:
            color = c
        else:
            color = [255, 255, 255]

        colors = tuple(color + color)

        return self.batch.add(
            2, pyglet.gl.GL_LINES, None,
            ('v2f', (p1.x, p1.y, p2.x, p2.y)),
            ('c3B', colors),
        )


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




def manual_update():
    global bricks
    if len(bricks) == 0:
        vl = batch.add(
            4, pyglet.gl.GL_POLYGON, None,
            ('v2f', (0,0,0,10,20,10,20,0)),
            ('c3B', (255, 255, 0,255, 255, 0,255, 255, 0,255, 255, 0,)),
        )
        bricks.append(vl)

    else:
        bricks[0].vertices = [n+10 for n in bricks[0].vertices]
        print('ok')


#AUTO LOOP
def auto_update(dt):
    pass


@window.event
def on_draw():
    window.clear()
    batch.draw()
    # pyglet.graphics.draw(
    #   3, pyglet.gl.GL_POINTS,
 #      ('v2i', (10, 15, 30, 35, 100, 100)),
 #      ('c3B', (255, 255, 0, 255, 0, 0, 50, 0, 255))
    # )
    # pyglet.gl.glLineWidth(8)
    # pyglet.graphics.draw(
    #   2, pyglet.gl.GL_LINES,
    #   ('v2f', (10, 15, 1000, 1000)),
    #   ('c3B', (255, 255, 0, 255, 0, 255)),
    # )
    # pyglet.graphics.draw(
    #   4, pyglet.gl.GL_POLYGON,
    #   ('v2f', (0,0,0,10,20,10,20,0)),
    #   ('c3B', (255, 255, 0,255, 255, 0,255, 255, 0,255, 255, 0,)),
    # )


    @window.event
    def on_key_press(symbol, modifiers):
        print('A key was pressed')
        manual_update()



if __name__ == "__main__":
    # Update the game 120 times per second
    if AUTO_LOOP:
        pyglet.clock.schedule_interval(auto_update, 1 / 15.0)  # AUTO LOOP

    # Tell pyglet to do its thing
    pyglet.app.run()
