"""Advent of Code 2023 -- Day 2: Cube Conundrum.

Reference: https://adventofcode.com/2023/day/2
"""
import math

from jibaoc import solver


class D02(solver.Solver):
    """Solve puzzle for day 2."""

    def __post_init__(self) -> None:
        """Initialize a D02 instance."""
        self._games: dict[int, dict[str, int]] = self._parse_game_data()

    def part_one(self) -> int:
        """Return the sum of the possible game IDs."""
        return sum(
            game_number
            for game_number, cube_counts in self._games.items()
            if cube_counts["red"] <= 12
            and cube_counts["green"] <= 13
            and cube_counts["blue"] <= 14
        )

    def part_two(self) -> int:
        """Return the sum of the power of each set of cubes."""
        return sum(math.prod(game_data.values()) for game_data in self._games.values())

    def _parse_game_data(self) -> dict[int, dict[str, int]]:
        """Parse game data and return it as a dictionary, keyed on game ID."""
        games: dict[int, dict[str, int]] = {}
        for line in self.pi.as_list_of_strings():
            cube_counts: dict[str, int] = {"red": 0, "green": 0, "blue": 0}
            game, draws = line.split(":", 1)
            game_number: int = int(game.split(" ", 1)[1])
            for draw in draws.split(";"):
                for count_color in draw.strip().split(","):
                    count, color = count_color.strip().split(" ", 1)
                    cube_counts[color] = max(int(count), cube_counts[color])
            games[game_number] = cube_counts
        return games
