
import functools
import operator


def spell_reducer(spells: list[int], operation: str) -> int:
    ops = {
        'add': operator.add,
        'multiply': operator.mul,
        'max': lambda a, b: a if a > b else b,
        'min': lambda a, b: a if a < b else b,
    }
    return functools.reduce(ops[operation], spells)


def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:
    return {
        'fire_enchant': functools.partial(
            base_enchantment, power=50, element='fire'
        ),
        'ice_enchant': functools.partial(
            base_enchantment, power=60, element='ice'
        ),
        'lightning_enchant': functools.partial(
            base_enchantment, power=70, element='lightning'
        ),
    }


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    """
    Calculate the nth Fibonacci number using memoization.
    This function uses the @lru_cache decorator to store previously
    computed values.

    maxsize=None
    The cache can grow without limit

    Without memoization:
        Time: O(2^n)

    With memoization:
        Time: O(n)
        Space: O(n)

    Huge improvement.
    """
    if n <= 1:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> callable:
    """
    Key idea:
    singledispatch creates a type-based function dispatcher
    similar to method overloading in languages like Java or C++.

    Why ?
    singledispatch is useful when you want clean polymorphism without
    lots of if isinstance() checks.
    """
    @functools.singledispatch
    def cast(spell):
        return f"Unknown spell type: {spell}"

    @cast.register(int)
    def _(spell: int):
        return f"Damage spell: {spell} damage dealt"

    @cast.register(str)
    def _(spell: str):
        return f"Enchantment: {spell} applied"

    @cast.register(list)
    def _(spell: list):
        return f"Multi-cast: {len(spell)} spells cast"

    return cast


if __name__ == "__main__":
    spells = [10, 20, 30, 40]
    print("\nTesting spell reducer...")
    print(f"Sum: {spell_reducer(spells, 'add')}")
    print(f"Product: {spell_reducer(spells, 'multiply')}")
    print(f"Max: {spell_reducer(spells, 'max')}")
    print(f"Min: {spell_reducer(spells, 'min')}")

    print("\nTesting partial enchanter...")

    def base_enchantment(item_name: str, power: int, element: str) -> str:
        return f"'{element.upper()} {item_name}' with power {power}"

    enchanter = partial_enchanter(base_enchantment)
    print(enchanter['fire_enchant']("Sword"))
    print(enchanter['ice_enchant']("Shield"))
    print(enchanter['lightning_enchant']("Bow"))

    print("\nTesting memoized fibonacci...")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")
    """
    # EXTRA TESTS

    # Normal version
    import time

    def fibonacci(n):
        if n <= 1:
            return n
        return fibonacci(n-1) + fibonacci(n-2)

    n = 40
    start = time.perf_counter()
    print(fibonacci(n))
    end = time.perf_counter()
    print("Normal time:", end - start)

    # Memoized version
    start = time.perf_counter()
    print(memoized_fibonacci(n))
    end = time.perf_counter()
    print("Memoized time:", end - start)
    """

    print("\nTesting spell dispatcher...")
    dispatcher = spell_dispatcher()
    print(dispatcher(10))
    print(dispatcher("Invisibility"))
    print(dispatcher([5, 15, 25]))
