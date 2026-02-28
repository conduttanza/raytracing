#28/02/2026
class Config():
    #OBJECTS
    screenSize = 1
    cameraPos = (0,0,-1)
    cameraFov = 70
    sphereCoordsRadius = (0,0,5,2)
    objects = [sphereCoordsRadius]
    #
    side = 500
    halfSide = side/2
    # ray intersection tolerance in radians (use larger to be more permissive)
    ray_tolerance = 36000/side**2
    #
    WHITE = (255,255,255)
    BLUE = (0,0,255)
    RED = (255,0,0)
    GREEN = (0,255,0)
    BLACK = (0,0,0)