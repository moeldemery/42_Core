#!/usr/bin/env python3

def ft_count_harvest_iterative():
    h_days = int(input("Days until harvest: "))
    for i in range(h_days):
        print("Day", i+1)
    print("Harvest time!")
