#!/usr/bin/env python3
class SecurePlant:
    def __init__(self, name:str, height:int, age:int):
        self.name = name
        self._height = height
        self._age = age
        print(f"Plant created: {self.name}")

    def display_info(self) -> None:
        print(f"Current plant: {self.name} ({self._height}cm, {self._age} days)")
    
    def set_height(self, new_height:int):
        if new_height >= 0:
            self._height = new_height
            print(f"Height updated: {self._height}cm [OK]")
        else:
            print(f"Invalid operation attempted: height {new_height}cm [REJECTED]")
            print("Security: Negative height rejected")
            
    def set_age(self, new_age:int) -> None:
        if new_age >= 0:
            self._age = new_age
            print(f"Age updated: {self._age}cm [OK]")
        else:
            print(f"Invalid operation attempted: age {new_age}days [REJECTED]")
            print("Security: Negative age rejected")
            
    def get_height(self) -> int:
        return self._height
    
    def get_age(self) -> int:
        return self._age
        
if __name__ == "__main__":
    print("=== Garden Security System ===")
    plant1 = SecurePlant("Rose", 25, 30)
    plant1.set_height(25)
    plant1.set_age(30)
    plant1.set_height(-5)
    plant1.display_info()
    
