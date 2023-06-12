#!/usr/bin/python3
def remove_char_at(string, n):
    if n >= 0:
        modified_string = string[:n] + string[n+1:]
    else:
        modified_string = string[:n] + string[n:]
    return modified_string
