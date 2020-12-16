from robot import Robot
from location import Location, Face
from enum import Enum
import config

class Table:
    def __init__(self, units=config.UNITS):
        self.units = units # units number in the square tables
        self.robot = Robot() # robot object
        
        # dictionary for the robot commands:
        # Key: is the command from the user
        # Value: method need to execute when command recieved
        self.commands_dict = {
            'PLACE' : self.place,
            'MOVE'  : self.move,
            'LEFT'  : self.left,
            'RIGHT' : self.right,
            'REPORT': self.report
        }
    
    # to get robot status 
    def __str__(self):
        return str(self.robot)

    # check if the robot will fall if move 1 unit to the direction it's facing
    def is_robot_fall(self):
        return (self.robot.location.f == Face.NORTH and self.robot.location.y == self.units - 1 or
                self.robot.location.f == Face.EAST  and self.robot.location.x == self.units - 1 or
                self.robot.location.f == Face.SOUTH and self.robot.location.y == 0              or
                self.robot.location.f == Face.WEST  and self.robot.location.x == 0)

    # check if location is a valid location on the giving table
    def is_valid_place(self, location):
        return (location.x < self.units  and  location.x >= 0 and 
                location.y < self.units  and  location.y >= 0 and
                location.f >= Face.NORTH and  location.f <= Face.WEST)

    # place robot in specific place
    def place(self, *args):
        if len(args) != 3: # PLACE command takes (X, Y, F) 
            return

        # check if parameters are valid
        if (args[0].isnumeric() == False or 
            args[1].isnumeric() == False or 
            not (args[2] in Face.__dict__)):
            return
        # parse the parameters to location object and pass it to the robot
        loc = Location(int(args[0]), int(args[1]), Face[str(args[2])])
        if self.is_valid_place(loc):
            self.robot.place(loc)

    def move(self, *args):
        if len(args) > 0:
            return
            # check if the robot will move without falling them move it
        if not self.is_robot_fall():
            self.robot.move()

    # rotate clockwise
    def right(self, *args):
        if len(args) > 0:
            return
        self.robot.right()

    # rotate anticlockwise
    def left(self, *args):
        if len(args) > 0:
            return
        self.robot.left()
    
    def report(self, *args):
        if len(args) > 0:
            return
        self.robot.report()
