# !/usr/bin/python
import os
import sys
import CodeWriter
import Parser


def main():
    file_name = sys.argv[1]                                                                     #gets the file from CLI
    parser = Parser.Parser(file_name + ".vm")                                                   #constructs the parser
    writer = CodeWriter.CodeWriter(file_name + ".asm")                                          #constructs the code writer

    while parser.hasMoreCommands():                                                             #checks if EOF
        parser.advance()                                                                        #gets the next line
        command_type = parser.commandType()                                                     #gets the command type
        if command_type == "push" or command_type == "pop":                                     #in case of push or pop
            writer.writePushOrPopCommand(command_type, parser.argument_segment(), parser.argument_value())
        elif command_type == "math":                                                            #in case of arithmetic command
            writer.writeArithmetic(parser.command[0])
        else:
            writer.writeError()

if __name__ == "__main__":
    main()