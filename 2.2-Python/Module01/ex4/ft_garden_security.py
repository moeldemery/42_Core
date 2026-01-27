#!/usr/bin/env python3
class SecurePlant:
    def __init__(self, name:str, height:int, age:int):
        self.name = name
        self.height = height
        self.current_age = age
        self.ft_get_info()

    def ft_get_info(self):
        print(f"Created: {self.name} ({self.height}cm, {self.current_age} days)")

if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    plants = [
        Plant("Rose", 25, 30),
        Plant("Oak", 200, 365),
        Plant("Cactus", 15, 120),
        Plant("Sunflower", 80, 45),
        Plant("Fern", 15, 120)
    ]
    print(f"Total plants created: {len(plants)}")
    
