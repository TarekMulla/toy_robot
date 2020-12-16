from location import Location, Face

# type represent robot and its main commands
class Robot:
    def __init__(self, x=0, y=0, f=Face.NONE):
        self.location = Location(x, y, f)
        self.start = False # robot will not accept any command till enable start flag 

    def __str__(self):
        return str(self.location)

    def is_ready(self):
        return self.start

    def place(self, location):
        self.location = location
        self.start = True # Activate the robot

    # move robot one unit based on the direction face
    def move(self):
        if self.is_ready():
            if self.location.f == Face.EAST:
                self.location.x += 1
            elif self.location.f == Face.WEST:
                self.location.x -= 1
            elif self.location.f == Face.NORTH:
                self.location.y += 1
            elif self.location.f == Face.SOUTH:
                self.location.y -= 1

    # rotate the robot 90 degrees anticlockwise
    def left(self):
        if self.is_ready():
            self.location.f = Face((self.location.f + 3) % 4) 

    # rotate the robot 90 degrees Clockwise
    def right(self):
        if self.is_ready():
            self.location.f = Face((self.location.f + 1) % 4) 

    # report robot status (location)
    def report(self):
        if self.is_ready():
            print(f"Output: {self}")

