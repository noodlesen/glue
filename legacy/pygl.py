# FIRST TEST

import pyglet
from random import randint

ball_image = pyglet.image.load('flake/flake_00000.png')


window = pyglet.window.Window(1920,1080)
batch = pyglet.graphics.Batch()

flakes = [
    pyglet.resource.image(
        "flake/flake_"+"{:05d}".format(f)+".png"
    )
    for f in range(1,100)
]


ani = pyglet.image.Animation.from_image_sequence(flakes, period=1/25, loop=True)

    
ball_sprites = []
for i in range(10000):
    x = randint(0,1920)
    y = randint(0,1080)
    sp = pyglet.sprite.Sprite(ani, x, y, batch=batch)
    sp.scale = randint(1,100)/500+0.1
    ball_sprites.append(sp)

def update(dt):
    for i, s in enumerate(ball_sprites):
        s.x+=i/10


@window.event
def on_draw():
    window.clear()
    #batch.draw()
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
    pyglet.graphics.draw(
        4, pyglet.gl.GL_POLYGON,
        ('v2f', (0,0,0,10,20,10,20,0)),
        ('c3B', (255, 255, 0,255, 255, 0,255, 255, 0,255, 255, 0,)),
    )


    



if __name__ == "__main__":
    # Update the game 120 times per second
    pyglet.clock.schedule_interval(update, 1 / 15.0)

    # Tell pyglet to do its thing
    pyglet.app.run()
