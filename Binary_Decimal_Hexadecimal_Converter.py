'''
Author: Blaine Wissler
Date: February 8, 2022
Description: Back end code for converting between binary, decimal, and hexadecimal values.
'''

def unsigned_binary_to_decimal(b):
    '''Converts an unsigned binary value (string) to its equivalent decimal value (int)'''
    exponent = 0
    value = 0
    for i in range(len(b) - 1, -1, -1):
        if b[i] == '1':
            value += 2**exponent
        exponent += 1
    return value

def decimal_to_binary(d):
    '''Converts a decimal value (int) into its equivalent binary value (string)'''
    b = ''
    while d > 0:
        digit = str(d % 2)
        b = digit + b
        d = d//2
    return b

def unsigned_hex_to_decimal(h):
    '''Converts an unsigned hexadecimal value (string) into its equivalen decimal value (int)'''
    hex_to_decimal = {'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}
    exponent = 0
    value = 0
    for i in range(len(h) - 1, -1, -1):
        if h[i] in hex_to_decimal:
            value += hex_to_decimal[h[i]] * 16 ** exponent
        else:
            value += int(h[i])* 16 ** exponent
        exponent += 1
    return value

def unsigned_hex_to_binary(h):
    '''Converts an unsigned hexadecimal value (string) into its equivalent binary value (string)'''
    d = unsigned_hex_to_decimal(h)
    return decimal_to_binary(d)




print(unsigned_binary_to_decimal('10101010'))
print(decimal_to_binary(4561347))
print(unsigned_hex_to_decimal('1FD23C'))
print(unsigned_hex_to_binary('1FD23C'))

