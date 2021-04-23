#!/usr/bin/env python3


class Parser():
    def __init__(self):
        self._a = 'a'
        self.__c = 'c'
        self.__d = 'd'

    def command_type(self, list):
        if list[0] == '@' and list[0] != '/':
            return self._a
        elif list[0] != '@' and list[0] != '/' and list[0] != '(':
            return self.__c
        return self.__d

    def dest(self, line):
        my_dest = ''
        if self.sign_exist(line, '='):
            for i in range(0, len(line)):
                if line[i] == '=':
                    break
                my_dest += line[i]
            return my_dest
        else:
            return 'null'

    def comp(self, line):
        my_comp = ''
        appeared = False
        if self.sign_exist(line, '='):
            for i in range(0, len(line)):
                if(appeared):
                    my_comp += line[i]
                if line[i] == '=':
                    appeared = True
            return my_comp
        elif self.sign_exist(line, ';'):
            for i in range(0, len(line)):
                if line[i] == ';':
                    break
                my_comp += line[i]
            return my_comp

    def jump(self, line):
        my_jump = ''
        appeared = False
        if self.sign_exist(line, ';'):
            for i in range(0, len(line)):
                if(appeared):
                    my_jump += line[i]
                if line[i] == ';':
                    appeared = True
            return my_jump
        return 'null'

    def sign_exist(self, line, sign):
        line = list(line)
        for i in range(0, len(line)):
            if line[i] == sign:
                return True
        return False