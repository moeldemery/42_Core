#!/usr/bin/env python3
import sys

if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    if len(sys.argv) <= 1:
        print(
            "No arguments provided!"
            " Usage: python3 ft_score_analytics.py <score1> <score2> ..."
        )
    else:
        scores: list[int] = []
        i = 1
        while i < len(sys.argv):
            try:
                val = int(sys.argv[i])
                scores.append(val)
            except ValueError:
                print(f"oops, I typed '{sys.argv[i]}' instead of ’1000’")
            i += 1
    if len(scores) > 0:
        total_players: int = len(scores)
        total_score: int = sum(scores)
        high_score: int = max(scores)
        low_score: int = min(scores)
        score_range: int = high_score - low_score
        average_score: float = total_score / total_players

        print(f"Scores processed: {scores}")
        print(f"Total players: {total_players}")
        print(f"Total score: {total_score}")
        print(f"Average score: {average_score}")
        print(f"High score: {high_score}")
        print(f"Low score: {low_score}")
        print(f"Score range: {score_range}")
