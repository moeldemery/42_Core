#!/usr/bin/env python3
class Plant:

    def __init__(self, name: str, height: int) -> None:
        self.name = name
        self.height = height
        self.plant_type = "regular"

    def grow(self, cm: int = 1) -> None:
        self.height += cm


class FloweringPlant(Plant):

    def __init__(self, name: str, height: int, color: str) -> None:
        super().__init__(name, height)
        self.color = color
        self.plant_type = "flowering"

    def status(self) -> str:
        return f"{self.color} flowers (blooming)"


class PrizeFlower(FloweringPlant):

    def __init__(self, name: str, height: int,
                 color: str, points: int) -> None:
        super().__init__(name, height, color)
        self.points = points
        self.plant_type = "prize"


class GardenManager:
    total_managers = 0

    def __init__(self, owner: str) -> None:
        self.owner = owner
        self.plants: list[Plant] = []
        self._growth_tracker = 0
        GardenManager.total_managers += 1

    def add_plant(self, plant: Plant) -> None:
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.owner}'s garden")

    def simulate_growth(self) -> None:
        print(f"\n{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()
            self._growth_tracker += 1
            print(f"{plant.name} grew 1cm")

    def report(self) -> None:
        print(f"=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")
        p_types = {"regular": 0, "flowering": 0, "prize": 0}
        for p in self.plants:
            if p.plant_type == "prize":
                print(f"- {p.name}: {p.height}cm, {p.status()}, "
                      f"Prize points: {p.points}")
                p_types["prize"] += 1
            elif p.plant_type == "flowering":
                print(f"- {p.name}: {p.height}cm, {p.status()}")
                p_types["flowering"] += 1
            else:
                print(f"- {p.name}: {p.height}cm")
                p_types["regular"] += 1
        print(f"\nPlants added: {len(self.plants)}, "
              f"Total growth: {self._growth_tracker}cm")
        print(f"Plant types: {p_types['regular']} regular, "
              f"{p_types['flowering']} flowering, "
              f"{p_types['prize']} prize flowers")

    @classmethod
    def create_garden_network(cls, owners: list[str]) -> list['GardenManager']:
        return [cls(owner) for owner in owners]

    @staticmethod
    def validate_height(height: int) -> bool:
        return height >= 0

    class GardenStats:

        @staticmethod
        def calculate_score(plants: list[Plant]) -> int:
            score = 0
            for p in plants:
                # score += p.height
                if p.plant_type == "prize":
                    score += p.points
            return score


if __name__ == "__main__":
    print("=== Garden Management System Demo ===\n")

    managers = GardenManager.create_garden_network(["Alice", "Bob"])
    alice = managers[0]
    bob = managers[1]

    alice.add_plant(Plant("Oak Tree", 100))
    alice.add_plant(FloweringPlant("Rose", 25, "red"))
    alice.add_plant(PrizeFlower("Sunflower", 50, "yellow", 10))

    alice.simulate_growth()
    alice.report()
    print(f"\nHeight validation test: {GardenManager.validate_height(10)}")

    a_score = GardenManager.GardenStats.calculate_score(alice.plants)
    # bob.add_plant(Plant("Small Bush", 92))
    b_score = GardenManager.GardenStats.calculate_score(bob.plants)

    print(f"Garden scores - Alice: {a_score}, Bob: {b_score}")
    print(f"Total gardens managed: {GardenManager.total_managers}")
