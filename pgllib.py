import pyglet

def check_color(**kwargs):  # private
    c = kwargs.get('c', None)
    if c is not None:
        color = c
    else:
        color = [255, 255, 255]
    return color

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
        self.window = pyglet.window.Window(w, h)
        self.batch = pyglet.graphics.Batch()




    def set_auto_update(fn, rate):
        pyglet.clock.schedule_interval(fn, 1 / rate) 

    def draw_point2d(self, p, sz, **kwargs):
        color = check_color(**kwargs)
        pyglet.gl.glPointSize(sz)

        return self.batch.add(
            1, pyglet.gl.GL_POINTS, None,
            ('v2f', (p.x, p.y)),
            ('c3B', color)
        )


    def draw_line2d(self, p1, p2, **kwargs):
        w = kwargs.get('w', 0)
        if w > 0:
            pyglet.gl.glLineWidth(w)

        color = check_color(**kwargs)

        colors = tuple(color + color)

        return self.batch.add(
            2, pyglet.gl.GL_LINES, None,
            ('v2f', (p1.x, p1.y, p2.x, p2.y)),
            ('c3B', colors),
        )

    def draw_poly2d(self, ul, ur, lr, ll, **kwargs):

        color = check_color(**kwargs)

        colors = tuple(color*4)

        return self.batch.add(
            4, pyglet.gl.GL_POLYGON, None,
            ('v2f', (ul.x,ul.y,ur.x,ur.y,lr.x,lr.y,ll.x,ll.y)),
            ('c3B', colors),
        )

    def draw_rect2d(self, ul, pm1, pm2=None, **kwargs):
        if pm2 is None:  # 2 points method
            lr = pm1
        else:  # width & height method
            lr = C(
                ul.x + pm1,
                ul.y - pm2
            )

        ur = C(lr.x, ul.y)
        ll = C(ul.x, lr.y)
        lines = []
        lines.append(self.draw_line2d(ul, ur, **kwargs))
        lines.append(self.draw_line2d(ur, lr, **kwargs))
        lines.append(self.draw_line2d(lr, ll, **kwargs))
        lines.append(self.draw_line2d(ll, ul, **kwargs))
        return lines

    def run(p):
        pyglet.app.run()


class Vob():  # VISUAL OBJECT
    
    def __init__(self, name, gtype, vl, groups=[]):
        self.name = name
        self.gtype = gtype
        self.vl = vl
        self.groups = groups
