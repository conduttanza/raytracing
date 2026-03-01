#28/02/2026
import math
import time
from config import Config
from scene import movement

class raytracing():
    
    def rayTracing(self):
        self.move = movement()
        self.c = Config()
        #self.cameraPos = self.c.cameraPos
        # convert FOV from degrees to radians before using it in trig functions
        self.cameraFov = math.radians(self.c.cameraFov)
        screen = []

        #collisionPoints = self.buildObjects()
        #print(collisionPoints)
        collisionPoints = self.buildObjects()
        # small numerical helpers
        def _sub(a,b):
            return (a[0]-b[0], a[1]-b[1], a[2]-b[2])
        def _length(v):
            return math.sqrt(v[0]*v[0] + v[1]*v[1] + v[2]*v[2])
        def _normalize(v):
            l = _length(v)
            if l == 0:
                return (0.0,0.0,0.0)
            return (v[0]/l, v[1]/l, v[2]/l)
        def _dot(a,b):
            return a[0]*b[0] + a[1]*b[1] + a[2]*b[2]
        for row in range(0,self.c.side,int(self.c.side/20)):
            #print(row)
            for p in range(0,self.c.side,int(self.c.side/20)):
                p = [row,p,False]
                
                dx = p[0] - self.c.halfSide
                dy = p[1] - self.c.halfSide
                # compute ray direction in camera/projective space
                self.projectionDistance = self.c.halfSide / math.tan(self.cameraFov / 2)
                local = (dx, dy, self.projectionDistance)
                rayDir = _normalize(local)
                camera_pos = self.c.cameraPos

                # compare ray direction with direction to sampled object surface points
                # use dot-product threshold instead of fragile angle equality
                # use configurable tolerance from config (radians)
                cos_eps = math.cos(self.c.ray_tolerance)
                hit = False
                for i in collisionPoints:
                    # i is a world-space 3D point on object surface
                    dir_to_point = _normalize(_sub(i, camera_pos))
                    if _dot(rayDir, dir_to_point) >= cos_eps:
                        hit = True
                        break
                p[2] = hit
                #print('yo we done yet?',p[0]*self.c.side,' out of like ', self.c.side**2)
                screen.append(p)
        print('frame done')
        return screen
    
    def buildObjects(self):
        collidePoints = []
        for obj in getattr(self.move,'objects', self.c.objects):
            print(obj)
            radius = obj[1]
            for phi in range(0,180,15):
                for theta in range(0,360,15):
                    xProj = radius * math.sin(math.radians(phi)) * math.cos(math.radians(theta))
                    yProj = radius * math.sin(math.radians(phi)) * math.sin(math.radians(theta))
                    zProj = radius * math.cos(math.radians(phi))

                    point = (obj[0][0] + xProj,
                            obj[0][1] + yProj,
                            obj[0][2] + zProj)
                    #print(point)
                    collidePoints.append(point)
        return collidePoints
    