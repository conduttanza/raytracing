#28/02/2026
from config import Config
import math
from threading import Thread
import time

class movement():
    def __init__(self,init_v1=(0.0365,0.0183,0),init_v2=(-0.146,-0.073,0)):
        self.c = Config()
        self.objects = self.c.objects           # reference the list in config
        obj1, obj2 = self.objects[0], self.objects[1]

        self.mass1 = obj1[2]
        self.mass2 = obj2[2]
        self.p1 = tuple(obj1[0])
        self.p2 = tuple(obj2[0])

        self.v1 = init_v1
        self.v2 = init_v2

        self.dt = 0.01        # timestep
        self.G  = 10**-2        # gravitational constant (choose 1 for simplicity)

        Thread(target=self.run, daemon=True).start()

    def run(self):
        while True:
            self.step()
            # write the new positions back so the ray‑tracer sees them
            self.objects[0][0] = self.p1
            self.objects[1][0] = self.p2
            time.sleep(self.dt)

    def step(self):
        # vector helpers
        def sub(a, b):      return (a[0]-b[0], a[1]-b[1], a[2]-b[2])
        def add(a, b):      return (a[0]+b[0], a[1]+b[1], a[2]+b[2])
        def mul(v, s):      return (v[0]*s, v[1]*s, v[2]*s)
        def length(v):      return math.sqrt(v[0]*v[0] + v[1]*v[1] + v[2]*v[2])
        def normalize(v):
            l = length(v)
            return (v[0]/l, v[1]/l, v[2]/l) if l != 0 else (0.0,0.0,0.0)

        # separation vector from body 1 to body 2
        r = sub(self.p2, self.p1)
        dist = length(r)
        if dist == 0:
            return                         # avoid division by zero
        r_hat = normalize(r)

        # gravitational force magnitude
        F = self.G * self.mass1 * self.mass2 / (dist*dist)

        # accelerations on each mass
        a1 = mul(r_hat,  F / self.mass1)   # toward body 2
        a2 = mul(r_hat, -F / self.mass2)   # opposite direction

        # integrate velocities and positions (simple Euler)
        self.v1 = add(self.v1, mul(a1, self.dt))
        self.v2 = add(self.v2, mul(a2, self.dt))

        self.p1 = add(self.p1, mul(self.v1, self.dt))
        self.p2 = add(self.p2, mul(self.v2, self.dt))