#!/usr/bin/env python3
class Plant:
    def __init__(self, name:str, height:int, age:int):
        self.name = name
        self.height = height
        self.current_age = age

    def ft_get_info(self):
        print(f"{self.name}: {self.height}cm, {self.current_age} days old")

    def grow(self):
        self.height += 1

    def age(self):
        self.current_age += 1

if __name__ == "__main__":
    
    p1 = Plant("Rose", 25, 30)
    print("=== Day 1 ===")
    p1.ft_get_info()
    old_height = p1.height
    for i in range(1,7):
        p1.grow()
        p1.age()

    print("=== Day 7 ===")
    p1.ft_get_info()
    new_height = p1.height
    grow_height = new_height - old_height
    print(f"Growth this week: +{grow_height}cm")
