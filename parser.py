import sys
from table import Table

class Parser:
    def __init__(self, table=Table()):
        self.table = table

    def parse_command(self, command_line):
        # check if command not empty
        if not command_line or command_line.isspace():
            return
        command = command_line.split()[0] # get the command
        # get the command argumetns
        args = [x.strip() for x in command_line[len(command):len(command_line)].split(',')]
        args = list(filter(None, args))
        if command in self.table.commands_dict:
            self.table.commands_dict[command](*args) # execute the command

    # parse text and execute commands line by line
    def parse_text(self, text):
        # replace \\n with valid new line when the user pass commands in the terminal
        lines = text.replace("\\n", "\n").split("\n") 
        for line in lines: 
            self.parse_command(line.upper().strip())
        return str(self.table)

    def parse_file(self, file_path):
        try:
            # open the file, read the contents and execute commands line by line
            with open(file_path, 'r') as file:
                lines = file.readlines()
                for line in lines: 
                    self.parse_command(line.upper().strip())
                file.close()
        except IOError:
            #print("File not accessible")
            sys.exit(2)
        finally:
            return str(self.table)
