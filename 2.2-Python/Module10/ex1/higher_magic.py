
def spell_combiner(spell1: callable, spell2: callable) -> callable:
    def combined(*args, **kwargs):
        return (spell1(*args, **kwargs), spell2(*args, **kwargs))
    return combined


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    def amplified(*args, **kwargs):
        return base_spell(*args, **kwargs) * multiplier
    return amplified


def conditional_caster(condition: callable, spell: callable) -> callable:
    def caster(*args, **kwargs):
        try:
            should_cast = condition(*args, **kwargs)
        except TypeError:
            should_cast = condition()

        if should_cast:
            return spell(*args, **kwargs)
        return "Spell fizzled"
    return caster


def spell_sequence(spells: list[callable]) -> callable:
    def sequence(*args, **kwargs):
        return [spell(*args, **kwargs) for spell in spells]
    return sequence


if __name__ == "__main__":
    def fireball(target: str) -> str:
        return f"Fireball hits {target}"

    def heal(target: str) -> str:
        return f"Heals {target}"

    def damage(power: int) -> int:
        return power

    print("\nTesting spell combiner...")
    combined: callable = spell_combiner(fireball, heal)
    result = combined("Dragon")
    print(f"Combined spell result: {result[0]}, {result[1]}")
    print()

    print("\nTesting power amplifier...")
    mega: callable = power_amplifier(damage, 3)
    original: int = damage(10)
    amplified: int = mega(10)
    print(f"Original: {original}, Amplified: {amplified}")

    print()
    print("\nTesting conditional caster...")

    def is_night() -> bool:
        return True
    night_spell: callable = conditional_caster(is_night, fireball)
    print(night_spell("Goblin"))
