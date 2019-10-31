import pyglet

class C():

    def __init__(self, x, y, z=None):
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


    def set_auto_update(fn, rate):
        pyglet.clock.schedule_interval(fn, 1 / rate) 


    def line2d(self, p1, p2, **kwargs):
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

    def poly2d(self, ul, ur, lr, ll, **kwargs):

        c = kwargs.get('c', None)
        if c is not None:
            color = c
        else:
            color = [255, 255, 255]

        colors = tuple(color*4)

        return self.batch.add(
            4, pyglet.gl.GL_POLYGON, None,
            ('v2f', (ul.x,ul.y,ur.x,ur.y,lr.x,lr.y,ll.x,ll.y)),
            ('c3B', colors),
        )

    def run(p):
        pyglet.app.run()


class Vob():  # VISUAL OBJECT
    
    def __init__(self, name, gtype, vl, groups=[]):
        self.name = name
        self.gtype = gtype
        self.vl = vl
        self.groups = groups
