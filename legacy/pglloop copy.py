from pgllib import Pgl, C
from random import randint
import pyglet

W = 1400
H = 800

AUTO_LOOP = False

pgl = Pgl(w=W, h=H)
# window = pyglet.window.Window(W,H)
# batch = pyglet.graphics.Batch()

frames = []
bricks = []


def manual_update():
    global bricks
    if len(bricks) == 0:
        p1 = C(0, 20)
        vl = pgl.poly2d(
            p1,
            C(40, 20),
            C(40, 0),
            C(0, 0),
            c = (255,255,0)
        )
        bricks.append(vl)

    else:
        bricks[0].vertices = [n+10 for n in bricks[0].vertices]
        print('ok')


#AUTO LOOP
def auto_update(dt):
    pass


@pgl.window.event
def on_draw():
    pgl.window.clear()
    pgl.point2d(C(200,200), 50, c=[255, 0, 0])
    pgl.point2d(C(300,300), 10, c=[0, 0, 255])
    pgl.batch.draw()

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


    @pgl.window.event
    def on_key_press(symbol, modifiers):
        print('A key was pressed')
        manual_update()



if __name__ == "__main__":
    # Update the game 120 times per second
    if AUTO_LOOP:
        #pyglet.clock.schedule_interval(auto_update, 1 / 15.0)  # AUTO LOOP
        pgl.set_auto_update(auto_update, 15)

    # Tell pyglet to do its thing
    #pyglet.app.run()
    pgl.run()
