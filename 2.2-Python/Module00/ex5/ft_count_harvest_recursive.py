#!/usr/bin/env python3

def ft_print_day(x, y):
    if x < y:
        print("Day", x + 1)
        ft_print_day(x + 1, y)


def ft_count_harvest_recursive():
    h_days = int(input("Days until harvest: "))
    ft_print_day(0, h_days)
    print("Harvest time!")
