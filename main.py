from parser import Parser
from table import Table
from toyrobot_test import Toyrobot_test
import config
import unittest, sys, getopt
from os import path

def main(argv):
    # help text to show in terminal
    help_txt = "\n\
-------------------- Toy robot ---------------------------\n\
main.py -h -f <commands_file> -c <commands> -u <units>\n\
    -h : help\n\
    -f : path to the commands file\n\
    -c : commands text\n\
    -u : square board size (in units)\n\n\
Each command should be separated by new line (\\n)\n\n\
Example1: python3 main.py -f 'test.txt' -u 5 \n\
Example2: python3 main.py -f 'test.txt'\n\
Example3: python3 main.py -c 'PLACE 0,0,NORTH\\nMOVE\\nREPORT'\n\
----------------------------------------------------------\n\n"

    commands_file = ''
    commands = ''
    units = config.UNITS

    # get all arguments passed by the user
    try:
        arguments, values = getopt.getopt(argv,"hf:c:u:",["help", "commands_file=", "command=", "units="])
    except getopt.GetoptError:
        print(help_txt)
        sys.exit(2)

    # parse the argument values
    for argument, value in arguments:
        if argument == '-h':
            print(help_txt)
            sys.exit()
        elif argument in ("-f", "--commands_file"):
            commands_file = value
        elif argument in ("-c", "--commands"):
            commands = value
        elif argument in ("-u", "--units"):
            if value.isnumeric():
                units = int(value)
    
    # check if units is valid
    if units < 1:
        print('Units provided not valid\n')
        sys.exit(2)
    
    # create a parser object after initialize the table object with Units number
    parser = Parser(Table(units))
    
    # check if the commands passed by the user are valid and start parsing it
    if (commands and not commands.isspace()):
        parser.parse_text(commands)
    elif (commands_file and not commands_file.isspace() and path.exists(commands_file)):
        parser.parse_file(commands_file)
    else:
        print('No commands provided, please use -h for more information\n')
        sys.exit(2)


# create suite for all unit tests in Toyrobot_test class
def create_suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(Toyrobot_test))
    return test_suite

# run all unittests exist in the toyrobost_test.py file
# and pass arguments to the main method 
if __name__ == '__main__':
    suite = create_suite()
    runner=unittest.TextTestRunner()
    runner.run(suite)
    main(sys.argv[1:])

