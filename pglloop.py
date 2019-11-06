from pgllib import Pgl, C
from pglui import Frame
from random import randint
import pyglet

W = 1400
H = 800

AUTO_LOOP = False

pgl = Pgl(w=W, h=H)

frames = []
vobs = []

mf = Frame('main', main=True)

def manual_update():
    pass

#AUTO LOOP
def auto_update(dt):
    pass


@pgl.window.event
def on_draw():
    pgl.window.clear()
    #
    pgl.batch.draw()


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
