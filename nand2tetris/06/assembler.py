#!/usr/bin/env python3

import Code
import Parser
import symbolTable


def main():
    my_symbols = symbolTable.SymbolTable()
    my_parser = Parser.Parser()
    my_code = Code.Code()
    line_number = 0
    file = open("Pong.asm", 'r')
    test = open("pongTest.hack", 'w')
    for line in file:
        l = line.split()
        if l == [] or l[0][0] == '/':
            continue
        if l[0][0] == '(':
            my_symbols.add_symbol(l[0], line_number, 'ok')
        else:
            line_number += 1

    file.seek(0)
    for line in file:
        line_number += 1
        l = line.split()
        if l == [] or l[0] == '/':
            continue
        adrress = ''
        if my_parser.command_type(l[0]) == 'a':
            if l[0][0] == '@':
                if not my_symbols.contains(l[0]):
                    my_symbols.add_symbol(l[0], line_number+1, 'n')
                if not l[0][1].isnumeric():
                    adrress = format(my_symbols.get_value(l[0]), '016b')
                    test.write(adrress)
                    test.write('\n')
                else:
                    number = ''
                    s = list(l[0])
                    s.pop(0)
                    for i in range(0, len(s)):
                        number += s[i]
                    test.write(format(int(number), '016b'))
                    test.write('\n')
        if my_parser.command_type(l[0]) == 'c':
            c = my_parser.comp(l[0])
            d = my_parser.dest(l[0])
            j = my_parser.jump(l[0])
            adrress = '111' + my_code.comp(c) + my_code.dest(d) + my_code.jump(j)
            test.write(adrress)
            test.write('\n')


if __name__ == '__main__':
    main()
