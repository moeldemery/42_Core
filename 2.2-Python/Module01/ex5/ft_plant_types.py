#!/usr/bin/env python3
class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.current_age = age

    def ft_get_info(self) -> None:
        print(f"Created: {self.name} "
              f"({self.height}cm, {self.current_age} days)")


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int,
                 color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
        print(f"{self.name} (Flower): {self.height}cm,"
              f" {self.current_age} days, {self.color} color")

    def bloom(self) -> None:
        print(f"{self.name} is blooming beautifully!\n")


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int,
                 trunk_diameter: int) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        print(f"{self.name} (Tree): {self.height}cm, "
              f"{self.current_age} days, {self.trunk_diameter}cm diameter")

    def produce_shade(self) -> None:
        area = int((22 * self.trunk_diameter * self.trunk_diameter)/700)
        print(f"{self.name} provides {area} square meters of shade\n")


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int,
                 harvest_season: str, nutritional_value: str) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value
        print(f"{self.name} (Vegetable): {self.height}cm, "
              f"{self.current_age} days, {self.harvest_season}")
        print(f"{self.name} is rich in {self.nutritional_value}\n")


if __name__ == "__main__":
    print("=== Garden Plant Types ===\n")
    flower1 = Flower("Rose", 25, 30, "red")
    flower1.bloom()

    tree1 = Tree("Oak", 500, 1825, 50)
    tree1.produce_shade()

    veg1 = Vegetable("Tomato", 80, 90, "summer harvest", "vitamin C")

    flower2 = Flower("Sunflower", 35, 50, "yellow")
    flower2.bloom()

    tree2 = Tree("Willow", 700, 1000, 100)
    tree2.produce_shade()

    veg2 = Vegetable("Eggplant", 100, 15, "winter harvest", "vitamin D")
