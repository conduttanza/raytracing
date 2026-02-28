#28/02/2026
import pygame
from config import Config
from rays import raytracing
rt = raytracing()
from scene import movement

class Window():
    def __init__(self):
        movement()
        self.c = Config()
        self.running = True
        pygame.init()
        pygame.display.set_caption('ray-tracing')
        self.screen = pygame.display.set_mode((self.c.side,self.c.side))
        self.clock = pygame.time.Clock()
        self.update()
        
    def update(self):
        try:
            while self.running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False
                        
                self.screen.fill(self.c.BLACK)
                #print('here we go')
                self.main()
                
                pygame.display.flip()
                self.clock.tick(15)
        except KeyboardInterrupt:
            pygame.quit()
            
    def main(self):
        screen = []
        screen = rt.rayTracing()
        for p in screen:
            if p[2] == True:
                pygame.draw.circle(self.screen, self.c.WHITE, (p[0],p[1]), 1)
        
    
    
