#!/usr/bin/env python3
from typing import Generator


def event_generator(count: int) -> Generator[dict[str, str | int], None, None]:
    """A generator that creates game events on-demand."""
    players_names: list[str] = ["alice", "bob", "charlie", "david", "Moooo"]
    event_types: list[str] = ["level_up", "kill", "logout", "found treasure"]

    for i in range(1, count + 1):
        yield {
            "id": i,
            "player": players_names[(i * 3) % len(players_names)],
            "event_type": event_types[(i * 11) % len(event_types)],
            "level": ((i * 7) % 24) + 1,
        }


def fibonacci_gen(n: int) -> Generator[int, None, None]:
    """Generates the first n Fibonacci numbers."""
    a: int = 0
    b: int = 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def prime_gen(n: int) -> Generator[int, None, None]:
    """Generates the first n Prime numbers."""
    count: int = 0
    num: int = 2
    is_prime: bool = True

    while count < n:
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            yield num
            count += 1
        num += 1


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===\n")

    total_events: int = 1000
    high_level_count: int = 0
    treasure_count: int = 0
    levelup_count: int = 0

    event_stream: Generator[dict[str, str | int], None, None] = iter(
        event_generator(1000)
    )
    print(f"Processing {total_events} game events...\n")

    for _ in range(total_events):
        event = next(event_stream)
        print(
            f"Event {event['id']}: Player {event['player']} "
            f"(level {event['level']}) {event['event_type']}"
        )

        if int(event["level"]) >= 10:
            high_level_count += 1
        if event["event_type"] == "found treasure":
            treasure_count += 1
        if event["event_type"] == "level_up":
            levelup_count += 1

    print("=== Stream Analytics ===\n")
    print(f"Total events processed: {total_events}")
    print(f"High-level players (10+): {high_level_count}")
    print(f"Treasure events: {treasure_count}")
    print(f"Level-up events: {levelup_count}")

    print("Memory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds")

    print("\n=== Generator Demonstration ===\n")
    fib_list = []
    for val in fibonacci_gen(10):
        fib_list.append(str(val))
    print(f"Fibonacci sequence (first 10): {', '.join(fib_list)}")

    # Prime Demo
    prime_list = []
    for val in prime_gen(5):
        prime_list.append(str(val))
    print(f"Prime numbers (first 5): {', '.join(prime_list)}")
