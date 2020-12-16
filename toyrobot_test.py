import unittest
import config
from parser import Parser
from table import Table

class Toyrobot_test(unittest.TestCase):

    def test_move(self):
        steps = '\
            PLACE 0,0,NORTH\n\
            MOVE'
        parser = Parser(Table())
        self.assertEqual(parser.parse_text(steps), "0,1,NORTH")
    
    def test_place(self):
        steps = '\
            PLACE 3,2,WEST\n\
            MOVE'
        parser = Parser(Table())
        self.assertEqual(parser.parse_text(steps), "2,2,WEST")

    def test_many_place(self):
        steps = '\
            PLACE 3,2,WEST\n\
            MOVE\n\
            PLACE 1,1,SOUTH'
        parser = Parser(Table())
        self.assertEqual(parser.parse_text(steps), "1,1,SOUTH")

    def test_left_place(self):
        steps = '\
            PLACE 0,0,NORTH\n\
            LEFT'
        parser = Parser(Table())
        self.assertEqual(parser.parse_text(steps), "0,0,WEST")

    def test_right_place(self):
        steps = '\
            PLACE 0,0,NORTH\n\
            RIGHT'
        parser = Parser()
        self.assertEqual(parser.parse_text(steps), "0,0,EAST")

    def test_right_round_place(self):
        steps = '\
            PLACE 0,0,NORTH\n\
            RIGHT\n\
            RIGHT\n\
            RIGHT\n\
            RIGHT'
        parser = Parser(Table())
        self.assertEqual(parser.parse_text(steps), "0,0,NORTH")

    def test_left_round_place(self):
        steps = '\
            PLACE 0,0,NORTH\n\
            LEFT\n\
            LEFT\n\
            LEFT\n\
            LEFT'
        parser = Parser(Table())
        self.assertEqual(parser.parse_text(steps), "0,0,NORTH")

    def test_read_file(self):
        parser = Parser(Table())
        self.assertEqual(parser.parse_file("test.txt"), "3,3,NORTH")

    def test_read_non_exist_file(self):
        parser = Parser(Table())
        self.assertEqual(parser.parse_file("test1.txt"), "0,0,NONE")

    def test_no_place(self):
        steps = '\
            MOVE\n\
            LEFT'
        parser = Parser(Table())
        self.assertEqual(parser.parse_text(steps), "0,0,NONE")

    def test_wrong_places(self):
        steps = '\
            PLACE 0,-1,NORTH\n\
            PLACE 0,0,NORTH,0\n\
            PLACE 0,NORTH\n\
            PLACE\n\
            MOVE\n\
            PLACE 0,0,NORT\n\
            PLACE 8,0,NORTH\n\
            PLACE a,b,NORTH\n\
            LEFT'
        parser = Parser(Table())
        self.assertEqual(parser.parse_text(steps), "0,0,NONE")

    def test_wrong_commands(self):
        steps = '\
            PLACE 0,0,NORTH\n\
            LEFT 5\n\
            RIGHT LEFT\n\
            LEFT to\n\
            \n\
            ,,\n\
            12\n\
            REPORT PRINT\n\
            REPORT 99'
        parser = Parser(Table())
        self.assertEqual(parser.parse_text(steps), "0,0,NORTH")

    def test_fall_robot_south_west_corner(self):
        steps = '\
            PLACE 0,0,SOUTH\n\
            MOVE\n\
            RIGHT\n\
            MOVE'
        parser = Parser(Table())
        self.assertEqual(parser.parse_text(steps), "0,0,WEST")

    def test_fall_robot_north_east_corner(self):
        steps = f'\
            PLACE {config.UNITS-1},{config.UNITS-1},NORTH\n\
            MOVE\n\
            RIGHT\n\
            MOVE'
        parser = Parser(Table())
        self.assertEqual(parser.parse_text(steps), f"{config.UNITS-1},{config.UNITS-1},EAST")

    def test_fall_robot_north_west_corner(self):
        steps = f'\
            PLACE 0,{config.UNITS-1},NORTH\n\
            MOVE\n\
            LEFT\n\
            MOVE'
        parser = Parser(Table())
        self.assertEqual(parser.parse_text(steps), f"0,{config.UNITS-1},WEST")

    def test_fall_robot_south_east_corner(self):
        steps = f'\
            PLACE {config.UNITS-1},0,SOUTH\n\
            MOVE\n\
            LEFT\n\
            MOVE'
        parser = Parser(Table())
        self.assertEqual(parser.parse_text(steps), f"{config.UNITS-1},0,EAST")
