#28/02/2026
import pygame
from config import Config
import math
import time

class Window():
    def __init__(self):
        self.c = Config()
        self.running = True
        pygame.init()
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
                print('here we go')
                self.main()
                
                pygame.display.flip()
                self.clock.tick(30)
        except KeyboardInterrupt:
            pygame.quit()
            
    def main(self):
        screen = self.rayTracing()
        for p in screen:
            if p[2] == True:
                pygame.draw.circle(self.screen, self.c.WHITE, (p[0],p[1]), 1)
        
    def rayTracing(self):
        #self.cameraPos = self.c.cameraPos
        # convert FOV from degrees to radians before using it in trig functions
        self.cameraFov = math.radians(self.c.cameraFov)
        screen = []

        #collisionPoints = self.buildObjects()
        #print(collisionPoints)
        
        for row in range(0,self.c.side,10):
            #print(row)
            for p in range(0,self.c.side,10):
                p = [row,p,False]
                
                dx = p[0] - self.c.halfSide
                dy = p[1] - self.c.halfSide

                # simpler, more direct ray direction: point on the projection plane
                self.projectionDistance = self.c.halfSide / math.tan(self.c.cameraFov / 2)

                # the pixel on the near plane in camera space
                local = (dx, dy, self.projectionDistance)
                # normalize to get unit direction
                length = math.sqrt(local[0]**2 + local[1]**2 + local[2]**2)
                rayDir = (local[0]/length, local[1]/length, local[2]/length)
                rayOrigin = self.c.cameraPos
                #HO L'ANGOLO, ORA INTERSECA CON OGGETTO?
                '''
                for i in collisionPoints:
                    #print('we going da looong way', i)
                    dx_collision = i[0] - self.c.halfSide
                    dy_collision = i[1] - self.c.halfSide
                    
                    self.collisionDistance = self.projectionDistance + i[2]*self.c.side
                    self.verticalCollisionAngle = round(math.atan2(dy_collision, self.collisionDistance),2)
                    self.horizontaCollisionlAngle = round(math.atan2(dx_collision, self.collisionDistance),2)
                print('yo we done yet?',p[0]*self.c.side,' out of like ', self.c.side**2)
                '''
                p[2] = self.ray_intersects_sphere(rayOrigin,rayDir,self.c.sphereCoordsRadius)
                screen.append(p)
        print('frame done')
        return screen
    
    def ray_intersects_sphere(self, rayOrigin, rayDir, sphere):
        # sphere = (x, y, z, radius)
        cx, cy, cz, r = sphere

        # Vector from ray origin to sphere center
        L = (
            rayOrigin[0] - cx,
            rayOrigin[1] - cy,
            rayOrigin[2] - cz
        )

        a = rayDir[0]**2 + rayDir[1]**2 + rayDir[2]**2
        b = 2 * (rayDir[0]*L[0] + rayDir[1]*L[1] + rayDir[2]*L[2])
        c = (L[0]**2 + L[1]**2 + L[2]**2) - r**2

        delta = b*b - 4*a*c

        if delta < 0:
            # no real roots, ray misses
            return False

        sqrt_d = math.sqrt(delta)
        t0 = (-b - sqrt_d) / (2*a)
        t1 = (-b + sqrt_d) / (2*a)
        # valid if at least one intersection is in front of the origin
        return t0 > 0 or t1 > 0
    
    '''
    def buildObjects(self):
        collidePoints = []
        for obj in self.c.objects:
            radius = obj[3]
            for phi in range(0,180,10):
                for theta in range(0,360,10):
                    xProj = radius * math.sin(math.radians(phi)) * math.cos(math.radians(theta))
                    yProj = radius * math.sin(math.radians(phi)) * math.sin(math.radians(theta))
                    zProj = radius * math.cos(math.radians(phi))

                    point = (obj[0] + xProj,
                            obj[1] + yProj,
                            obj[2] + zProj)
                    #print(point)
                    collidePoints.append(point)
        return collidePoints
    '''