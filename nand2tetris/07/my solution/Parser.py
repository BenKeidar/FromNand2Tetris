#!/usr/bin/env python3

#initializing constructor with file name and eof
class Parser:
    def __init__(self, file_name):
        self.input_file = open(file_name)
        self.command = [""]
        self.end_of_file = False

        self.command_type = {
            "sub": "math",
            "add": "math",
            "neg": "math",
            "eq": "math",
            "gt": "math",
            "lt": "math",
            "and": "math",
            "or": "math",
            "not": "math",
            "push": "push",
            "pop": "pop",
            "EOF": "EOF",
        }

    #function that checks if the file has no more lines
    def hasMoreCommands(self):
        location = self.input_file.tell()
        self.advance()
        self.input_file.seek(location)
        return not self.end_of_file

    #function that checks every line for commands
    def advance(self):
        current_line = self.input_file.readline()
        if current_line == '':
            self.end_of_file = True
        else:
            split_line = current_line.split("/")[0].strip()
            if split_line == '':
                self.advance()
            else:
                self.command = split_line.split()

    #function that returns the command type
    def commandType(self):
        return self.command_type.get(self.command[0], "invalid command_type")

    #function that returns the segment
    def argument_segment(self):
        return self.command[1]

    #function that returns the value
    def argument_value(self):
        return self.command[2]