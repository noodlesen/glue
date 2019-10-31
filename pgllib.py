import pyglet

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

    def __init__(self, **kwargs):
        w = kwargs.get('w', 1920)
        h = kwargs.get('h', 1080)
        self.window = pyglet.window.Window(w,h)
        self.batch = pyglet.graphics.Batch()


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

    def run(p):
        pyglet.app.run()
