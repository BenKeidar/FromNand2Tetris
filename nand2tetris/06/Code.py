#!/usr/bin/env python3


class Code():
    def __init__(self):
        self._comp = {'0': '101010', '1': '111111', '-1': '111010', 'D': '001100', 'A': '110000',
                      'M': '110000', '!D': '001101', '!A': '110001', '!M': '110001', '-D': '001111',
                      '-A': '110011', '-M': '110011', 'D+1': '011111', 'A+1': '110111', 'M+1': '110111',
                      'D-1': '001110', 'A-1': '110010', 'M-1': '110010', 'D+A': '000010', 'D+M': '000010',
                      'D-A': '010011', 'D-M': '010011', 'A-D': '000111', 'M-D': '000111', 'D&A': '000000',
                      'D&M': '000000', 'D|A': '010101', 'D|M': '010101'}

        self._dest = {'null': '000', 'M': '001', 'D': '010', 'MD': '011', 'A': '100', 'AM': '101',
                      'AD': '110', 'AMD': '111'}

        self._jump = {'null': '000', 'JGT': '001', 'JEQ': '010', 'JGE': '011', 'JLT': '100', 'JNE': '101',
                      'JLE': '110', 'JMP': '111'}

    def comp(self, destination):
        if (destination == 'M' or destination == '!M' or destination == '-M' or destination == 'M+1' or
            destination == 'M-1' or destination == 'D+M' or destination == 'D-M' or destination == 'M-D' or
            destination == 'D&M' or destination == 'D|M'):
            res = '1' + self._comp[destination]

            return res
        else:
            res = '0' + self._comp[destination]
            return res


    def dest(self, destination):
        return self._dest[destination]

    def jump(self, destination):
        return self._jump[destination]
