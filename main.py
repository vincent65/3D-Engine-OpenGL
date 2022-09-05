import pygame as pg
import moderngl as mgl
import sys
from model import *
from camera import Camera

class GraphicsEngine:
    def __init__(self, win_size=(1600,900)):
        pg.init()
        self.WIN_SIZE = win_size

        #opengl attributes
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE)

        #create opengl context
        pg.display.set_mode(self.WIN_SIZE, flags = pg.OPENGL | pg.DOUBLEBUF)

        #detect and use the opengl context
        self.ctx = mgl.create_context()
        #keep track of time
        self.clock = pg.time.Clock()

    #exit when escape key is pressed
    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()

    def render(self):
        #clear the framebuffer
        self.ctx.clear(color=(0.08,0.16,0.18))
        #swap the buffers
        pg.display.flip()

    def run(self):
        while True:
            self.check_events()
            self.render()
            #set the framerate
            self.clock.tick(60)


if __name__ == '__main__':
    app = GraphicsEngine()
    app.run()