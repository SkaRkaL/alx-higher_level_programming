#!/usr/bin/python3
for ascii_value in range(97, 123):
    character = chr(ascii_value)
    if character == 'e' or character == 'q':
        continue
    print("{}".format(character), end="")
