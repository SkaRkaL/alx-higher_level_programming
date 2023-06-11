#!/usr/bin/python3

def print_hex(i):
    hex_value = hex(i)[2:]
    print("{} = 0x{}".format(i, hex_value))

for i in range(0, 99):
    print_hex(i)
