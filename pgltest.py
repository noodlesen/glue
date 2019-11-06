"""test drawing."""
from pgllib import C, Pgl
from pglui import Frame
from pglinit import pgl

W = 1400
H = 800




frames = []
vobs = []

mf = Frame('main', main=True)
mf.pd = 12
mf.rebuild()
s1, s2 = mf.split('v', 40)
s1.pd = 10
s2.pd = 10

s1.rebuild()
s2.rebuild()

def manual_update():
    pass



@pgl.window.event
def on_draw():
    pgl.window.clear()
    pgl.batch.draw()


@pgl.window.event
def on_key_press(symbol, modifiers):
    print('A key was pressed')
    manual_update()



if __name__ == "__main__":
    mf.draw_itself()
    s2.draw_itself()
    s1.draw_itself()
    pgl.run()
