
def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda a: a['power'], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda m: m['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda s: f"* {s} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    powers = list(map(lambda m: m['power'], mages))
    return {
        'max_power': max(powers),
        'min_power': min(powers),
        'avg_power': round(sum(powers) / len(powers), 2)
    }


def main():
    print()
    artifacts = [
        {'name': 'Crystal Orb', 'power': 85, 'type': 'orb'},
        {'name': 'Fire Staff', 'power': 92, 'type': 'staff'},
        {'name': 'Shadow Cloak', 'power': 60, 'type': 'armor'},
    ]
    print("Testing artifact sorter...")
    sorted_artifacts = artifact_sorter(artifacts)
    print(
        f"{sorted_artifacts[0]['name']} ({sorted_artifacts[0]['power']} power)"
        f" comes before"
        f" {sorted_artifacts[1]['name']} "
        f"({sorted_artifacts[1]['power']} power)"
    )
    print(f"\nMage stats: {mage_stats(sorted_artifacts)}")
    print("\nTesting power filter +70...")
    filtered_mages = power_filter(sorted_artifacts, 70)
    print(f"Filtered mages: {len(filtered_mages)}")
    print("\nTesting spell transformer...")

    spells = ["fireball", "heal", "shield"]
    transformed = spell_transformer(spells)
    print(" ".join(transformed))


if __name__ == "__main__":
    main()
