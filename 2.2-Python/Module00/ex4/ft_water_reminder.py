#!/usr/bin/env python3

def ft_water_reminder():
    w_days = int(input("Days since last watering: "))
    if (w_days > 2):
        print("Water the plants!")
    else:
        print("Plants are fine")
