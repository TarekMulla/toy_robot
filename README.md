# toy_robot assignment
----------------------
Command Line Arguments
----------------------

    main.py -h -f <commands_file> -c <commands> -u <units>
        -h : help
        -f : path to the commands file
        -c : commands text
        -u : square board size (in units)

    Each command should be separated by new line (\n)

    Example1: python3 main.py -f 'test.txt' -u 5 
    Example2: python3 main.py -f 'test.txt'
    Example3: python3 main.py -c 'PLACE 0,0,NORTH\nMOVE\nREPORT'


-------------------------
Setup and run
-------------------------

    The app accept 2 kinds of input:
        - From commands file
        - Plain text
    The user can pass the commands from the Terminal  

    To do quick test for the code, it just needs to initialize Parser object, 
    then call parse_text or parse_file method, example:
        parser = Parser()
        parser.parse_text('PLACE 0,0,NORTH\nMOVE')

    The table constructor take parameters for units number, be default is 5

    parse_file method take file path of commands file, example:
        parser = Parser()
        parser.parse_file("test.txt")

    The application is case insensitive to the commands, so MOVE same as move

    If need to add any new command just write a new action method in class (Table), 
    then add it to the commands_dict:
        Key     ->  Command
        Value   ->  the new method


-------------------------
Features
-------------------------

    * Can add many new commands by adding it to the dictionary in Table class (commands_dict)

    * Table units is dynamic

    * Read from commands file or plain text
    
    * Clean, well commented and tested code


-------------------------
Files in the project
-------------------------

    main.py:            Start point for the app, parse the args passed from terminal, 
                        initialize the robot and the table objects
                        then call the parsing method to start parse and execute the 
                        valid commmandes from the command file 

    parser.py:          Parse the commands file, or commands lines as text and execute 
                        the related methods linked to the commands in dictionary

    table.py:           Represent the table that robot move on it, do the necessary check
                        to avoid robot falling and unvalid placement

    location.py:        Has location class, and face enumeration to use in other files

    config.py:          Has the general setting of the application shared with all files

    toyrobot_test.py:   Contains all units and integration test


-------------------------
Unit tests covered 
-------------------------

    It has been convered 16 different cases in the assignment.

    Those cases are:
        * MOVE command
        * PLACE command
        * many PLACE commands
        * LEFT command
        * RIGHT cmmand
        * Many RIGHT commands (360 degrees)
        * Many LEFT commands (360 degrees)
        * Read from file
        * Read from file not exist
        * No PLACE command
        * Wrong PLACE command
        * Many different Unknown commands
        * Robot falling in the south west corner
        * Robot falling in the north east corner
        * Robot falling in the north west corner
        * Robot falling in the south east corner
