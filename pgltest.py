"""test drawing."""
from pgllib import C, Mob
from pglinit import pgl, DEFAULT_W, DEFAULT_H
import datetime

@pgl.window.event
def on_draw():
    pgl.window.clear()
    pgl.batch.draw()

@pgl.window.event
def on_mouse_motion(x, y, dx, dy):
    for v in pgl.vobs:
        if v.mob == chh:
            for n in range(0, len(v.vl.vertices)):
                if n%2==1:
                    v.vl.vertices[n] = y
        if v.mob == chv:
            for n in range(0, len(v.vl.vertices)):
                if n%2==0:
                    v.vl.vertices[n] = x


@pgl.window.event
def on_key_press(symbol, modifiers):
    pgl.last_keydown = datetime.datetime.now()
    pgl.last_key = symbol
    offs = 5
    if modifiers & pgl.key.MOD_SHIFT:
        offs = 25
        print('SHIFT')
    for v in pgl.vobs:
        if v.mob == sq:
            if symbol == pgl.key.UP:
                v.shift((0, offs))
            if symbol == pgl.key.RIGHT:
                v.shift((offs, 0))
            if symbol == pgl.key.DOWN:
                v.shift((0, -offs))
            if symbol == pgl.key.LEFT:
                v.shift((-offs, 0))

@pgl.window.event
def on_key_release(symbol, modifiers):
    pgl.last_keyup = datetime.datetime.now()

def auto_check(dt):
    if pgl.last_keyup < pgl.last_keydown and (pgl.last_keyup-datetime.datetime.now()).seconds > 1:
        print ('HOLD')



if __name__ == "__main__":
    pgl.set_auto_check(auto_check, 3)
    sq = Mob('square')
    pgl.draw_rect2d(C(250, 250), 100, 100, c=[255, 200, 10], mob=sq)
    chh = Mob('crosshair_h')
    pgl.draw_line2d(C(0,0), C(DEFAULT_W,0), c=[34,34,34], mob=chh)
    chv = Mob('crosshair_v')
    pgl.draw_line2d(C(0,0), C(0,DEFAULT_H), c=[34,34,34], mob=chv)
    pgl.run()
