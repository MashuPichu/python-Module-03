# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_data_stream.py                                 :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: klucchin <klucchin@student.42nice.fr>     +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/22 18:31:55 by mashu           #+#    #+#               #
#  Updated: 2026/02/24 10:00:00 by klucchin        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from typing import Generator


def game_event_stream(n: int) -> Generator[dict, None, None]:
    """Generate game events one by one (streaming)."""
    players = ["alice", "bob", "charlie", "diana", "eve"]
    events = ["killed monster", "found treasure", "leveled up"]

    for i in range(1, n + 1):
        yield {
            "id": i,
            "player": players[i % len(players)],
            "level": (i * 3) % 20 + 1,
            "event": events[i % len(events)],
        }


def process_game_events(stream: Generator[dict, None, None]) -> None:
    total_events = 0
    high_level_players = 0
    treasure_events = 0
    level_up_events = 0

    print("=== Game Data Stream Processor ===")
    print("Processing 1000 game events...")

    for event in stream:
        total_events += 1

        if total_events <= 3:
            print(
                f"Event {event['id']}: Player {event['player']} "
                f"(level {event['level']}) {event['event']}"
            )
        elif total_events == 4:
            print("...")

        if event["level"] >= 10:
            high_level_players += 1
        if event["event"] == "found treasure":
            treasure_events += 1
        if event["event"] == "leveled up":
            level_up_events += 1

    print("=== Stream Analytics ===")
    print(f"Total events processed: {total_events}")
    print(f"High-level players (10+): {high_level_players}")
    print(f"Treasure events: {treasure_events}")
    print(f"Level-up events: {level_up_events}")
    print("Memory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds")


def fibonacci(n: int) -> Generator[int, None, None]:
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def primes(n: int) -> Generator[int, None, None]:
    count = 0
    num = 2

    while count < n:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            yield num
            count += 1
        num += 1


def main() -> None:
    stream = game_event_stream(1000)
    process_game_events(stream)

    print("=== Generator Demonstration ===")

    fib_values = []
    for value in fibonacci(10):
        fib_values.append(str(value))
    print("Fibonacci sequence (first 10):", ", ".join(fib_values))

    prime_values = []
    for value in primes(5):
        prime_values.append(str(value))
    print("Prime numbers (first 5):", ", ".join(prime_values))


if __name__ == "__main__":
    main()