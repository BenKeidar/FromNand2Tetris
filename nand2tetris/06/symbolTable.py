#!/usr/bin/env python3


class SymbolTable():
    def __init__(self):
        self._n = 16
        self._symbols = {'SCREEN': 16384, 'KBD': 24576, 'SP': 0, 'LCL': 1, 'ARG': 2, 'THIS': 3, 'THAT': 4}
        for i in range(0, self._n):
            self._symbols['R'+str(i)] = i

    def add_symbol(self, symbol, address, sign):
        if not str(symbol[1]).isnumeric():
            if sign == 'n':
                if str(symbol).islower():
                    address = self._n
                    self._n += 1
                else:
                    s = list(symbol)
                    s.pop(0)
                    symbol = '('
                    for i in s:
                        symbol += i
                    symbol += ')'
            self._symbols[symbol] = address

    def contains(self, symbol):
        old = symbol
        temp = list(symbol)
        temp.pop(0)
        symbol = ''
        for i in temp:
            symbol += i
        s = '(' + symbol + ")"
        if symbol in self._symbols.keys() or s in self._symbols.keys() or old in self._symbols.keys():
            return True
        return False

    def get_value(self, key):
        if key in self._symbols:
            return self._symbols[key]
        elif key[0] != '@':
            return self._symbols[key]
        else:
            if key not in self._symbols:
                s = list(key)
                s.pop(0)
                justname = ''
                newkey = '('
                for i in s:
                    justname += i
                    newkey += i
                newkey += ')'
                if newkey in self._symbols:
                    return self._symbols[newkey]
                else:
                    return self._symbols[justname]

    def __str__(self):
        my_dict = ''
        for k,v in self._symbols.items():
            t = k + ': ' + str(v) + '\n'
            my_dict += t
        return my_dict