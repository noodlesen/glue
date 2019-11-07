"""test drawing."""
from pgllib import C, Mob
from pglinit import pgl


@pgl.window.event
def on_draw():
    pgl.window.clear()
    pgl.batch.draw()


@pgl.window.event
def on_key_press(symbol, modifiers):
    offs = 5
    if modifiers & pgl.key.MOD_SHIFT:
        offs=25
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


if __name__ == "__main__":
    sq = Mob('square')
    pgl.draw_rect2d(C(250, 250), 100, 100, c=[255, 200, 10], mob=sq)
    #pgl.draw_point2d(C(250, 250), 10, c=[255, 200, 10], mob=sq)
    pgl.run()
