#!/usr/bin/python3

def print_hex(i):
    hex_value = hex(i)[2:]
    print(i, end=" = 0x" + hex_value + "\n")

for i in range(0, 99):
    print_hex(i)
