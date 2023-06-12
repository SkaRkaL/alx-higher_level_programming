#!/usr/bin/python3
def remove_char_at(string, n):
    modified_string = string[:n] + string[n+1:]
    return modified_string
