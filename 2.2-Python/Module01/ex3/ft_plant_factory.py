#!/usr/bin/env python3
class Plant:
    def __init__(self, name:str, height:int, age:int):
        self.name = name
        self.height = height
        self.current_age = age

    def ft_get_info(self):
        print(f"Created: {self.name} ({self.height}cm, {self.current_age} days)")

if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    p1 = Plant("Rose", 25, 30)
    p2 = Plant("Sunflower", 80, 45)
    p3 = Plant("Cactus", 15, 120)
