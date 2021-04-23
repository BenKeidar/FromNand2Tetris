# !/usr/bin/python

#initializing constructor with file name and label index
class CodeWriter:
    def __init__(self, full_file_name):
        self.file_name = full_file_name[:-4].split('/')[-1]
        self.outfile = open(full_file_name, "w")
        self.next_label_index = 0

    #function that gets the translation to arithmetic commands from VM to assembly into file
    def writeArithmetic(self, command):
        output = ""
        if (command == "add") or (command == "sub"):
            output += self.writeAddOrSub(output, command)
        elif (command == "neg") or (command == "not"):
            output += self.writeNegOrNot(output, command)
        elif (command == "or") or (command == "and"):
            output += self.writeOr_And(output, command)
        elif (command == "eq") or (command == "gt") or (command == "lt"):
            output += self.writeComparisonCommand(output, command)
        self.outfile.write(output)

    #function that gets the translation to push/pop commands from VM to assembly into file
    def writePushOrPopCommand(self, command, segment, value):
        output = ""
        if command == "push":
            output += self.writePush(output, segment, value)
        elif command == "pop":
            output += self.writePop(output, segment, value)
        self.outfile.write(output)

    #in case of error in command weite wrong command to file
    def writeError(self):
        self.outfile.write("Wrong command\n")

    #function that translates push command corrsepoding to the command into assemly
    def writePush(self, output, segment, value):
        if (segment == "constant") or (segment == "static"):
            if segment == "constant":
                output += "@" + value + "\n" + "D=A\n"
            if segment == "static":
                output += "@" + self.file_name + "." + value + "\n" + "D=M\n"
            output += "@SP\n" + "A=M\n" + "M=D\n" + "@SP\n" + "M=M+1\n"
        elif (segment == "this") or (segment == "that") or (segment == "argument") or \
             (segment == "local") or (segment == "temp") or (segment == "pointer"):
            output += "@" + value + "\n" + "D=A\n"
            if segment == "this":
                output += "@THIS\n" + "A=M+D\n"
            elif segment == "that":
                output += "@THAT\n" + "A=M+D\n"
            elif segment == "argument":
                output += "@ARG\n" + "A=M+D\n"
            elif segment == "local":
                output += "@LCL\n" + "A=M+D\n"
            elif segment == "temp":
                output += "@5\n" + "A=A+D\n"
            elif segment == "pointer":
                output += "@3\n" + "A=A+D\n"
            output += "D=M\n" + "@SP\n" + "A=M\n" + "M=D\n" + "@SP\n" + "M=M+1\n"
        return output

    #function that translates pop command corrsepoding to the command into assemly
    def writePop(self, output, segment, value):
        if segment == "static":
            output += "@SP\n" + "AM=M-1\n" + "D=M\n" + "@" + self.file_name + "." + value + "\n" + "M=D\n"
        elif (segment == "this") or (segment == "that") or (segment == "argument") or \
                (segment == "local") or (segment == "pointer") or (segment == "temp"):
            output += "@" + value + "\n" + "D=A\n"
            if segment == "this":
                output += "@THIS\n" + "D=M+D\n"
            elif segment == "that":
                output += "@THAT\n" + "D=M+D\n"
            elif segment == "argument":
                output += "@ARG\n" + "D=M+D\n"
            elif segment == "local":
                output += "@LCL\n" + "D=M+D\n"
            elif segment == "pointer":
                output += "@3\n" + "D=A+D\n"
            elif segment == "temp":
                output += "@5\n" + "D=A+D\n"
            output += "@R13\n" + "M=D\n" + "@SP\n" + "AM=M-1\n" + "D=M\n" + "@R13\n" + "A=M\n" + "M=D\n"
        return output

    #function that writes the translation from add or sub command
    def writeAddOrSub(self, output, command):
        output += "@SP\n" + "AM=M-1\n" + "D=M\n" + "@SP\n" + "AM=M-1\n"
        if command == "add":
            output += "M=D+M\n"
        elif command == "sub":
            output += "M=M-D\n"
        output += "@SP\n" + "M=M+1\n"
        return output

    #function that writes the translation from neg or not command
    def writeNegOrNot(self, output, command):
        output += "@SP\n" + "A=M-1\n"
        if command == "neg":
            output += "M=-M\n"
        else:
            output += "M=!M\n"
        return output

    #function that writes the translation from or or and command
    def writeOr_And(self, output, command):
        output += "@SP\n" + "AM=M-1\n" + "D=M\n" + "@SP\n" + "A=M-1\n"
        if command == "or":
            output += "M=D|M\n"
        else:
            output += "M=D&M\n"
        return output

    #function that writes the translation from equal or lt or gt command
    def writeComparisonCommand(self, output, command):
        label_index = str(self.next_label_index)
        self.next_label_index += 1
        output += "@SP\n" + "AM=M-1\n" + "D=M\n" + "@SP\n" + "A=M-1\n" + "D=M-D\n" + "M=-1\n"
        if command == "eq":
            output += "@eq" + label_index + "\n" + "D;JEQ\n"
        if command == "gt":
            output += "@gt" + label_index + "\n" + "D;JGT\n"
        if command == "lt":
            output += "@lt" + label_index + "\n" + "D;JLT\n"
        output += "@SP\n" + "A=M-1\n" + "M=0\n"
        if command == "eq":
            output += "(eq" + label_index + ")\n"
        if command == "gt":
            output += "(gt" + label_index + ")\n"
        if command == "lt":
            output += "(lt" + label_index + ")\n"
        return output
