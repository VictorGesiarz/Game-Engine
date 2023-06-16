import pygame as pg

from player import Player

class App:
    def __init__(self) -> None:
        self.res = self.width, self.height = (800, 450)
        self.screen = pg.display.set_mode(self.res)
        self.FPS = 60
        self.clock = pg.time.Clock()
        
        self.player = Player()
        self.face = 
    
    def update(self):
        self.player.update()
    
    def draw(self):
        
        pg.display.flip()
    
    def run(self):
        while True:
            self.update()
            self.draw()
            
            [exit() for i in pg.event.get() if i.type == pg.QUIT]
            self.clock.tick(self.FPS)
            pg.display.set_caption(f'FPS: {self.clock.get_fps()}')
