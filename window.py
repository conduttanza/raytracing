#28/02/2026
import pygame
from config import Config
from rays import raytracing
rt = raytracing()
from scene import movement

class Window():
    def __init__(self):
        self.move = movement()
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
        if self.c.rayTracing == True:
            screen = []
            screen = rt.rayTracing()
            for p in screen:
                if p[2] == True:
                    pygame.draw.circle(self.screen, self.c.WHITE, (p[0],p[1]), 1)
        else:
            body1 = getattr(self.move,'p1', [0,0,0])
            body2 = getattr(self.move,'p2',[0,0,0])
            if body1[2] >= body2[2]:
                pygame.draw.circle(self.screen,(0,255/body1[2],0),(body1[0]*10+self.c.halfSide,body1[1]*20+self.c.halfSide),20)
                pygame.draw.circle(self.screen,(0,0,255/body2[2]),(body2[0]*10+self.c.halfSide,body2[1]*20+self.c.halfSide),5)
            if body1[2] <= body2[2]:
                pygame.draw.circle(self.screen,(0,0,255/body2[2]),(body2[0]*10+self.c.halfSide,body2[1]*20+self.c.halfSide),5)
                pygame.draw.circle(self.screen,(0,255/body1[2],0),(body1[0]*10+self.c.halfSide,body1[1]*20+self.c.halfSide),20)
        
    
    
