#!/usr/bin/python3
def ft_putchar(c):
    print(c, end='')

def ft_print_comb():
    b = 0
    while b <= 98:
        ft_putchar(chr(ord('0') + b // 10))
        ft_putchar(chr(ord('0') + b % 10))
        if b != 98:
            ft_putchar(',')
            ft_putchar(' ')
        b += 1

ft_print_comb()
print()
