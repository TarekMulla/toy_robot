import enum 

# enum repreesent facing direction
class Face(enum.IntEnum):
    NORTH   = 0
    EAST    = 1
    SOUTH   = 2
    WEST    = 3
    NONE    = 4

    def __str__(self):
        return self.name


# new type te represent the location of robot and the direction is face 
class Location:
    def __init__(self, x=-1, y=-1, f=Face.NONE):
        self.x = x
        self.y = y
        self.f = f
    
    # override __str__ to print and get robot status
    def __str__(self):
        return f"{self.x},{self.y},{self.f}"

