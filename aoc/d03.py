"""Advent of Code 2023 -- Day 3: Gear Ratios.

Reference: https://adventofcode.com/2023/day/3
"""
import dataclasses
import math
from typing import Final

from jibaoc import solver, space


@dataclasses.dataclass
class Number:
    """A potential part number, and the points in space where that number exists."""

    number: int
    points: set[space.Point]


class D03(solver.Solver):
    """Solve puzzle for day 3."""

    _GEAR_PART_COUNT: Final[int] = 2

    def __post_init__(self) -> None:
        """Initialize a D03 instance."""
        self._gear_locations: set[space.Point] = set()
        self._symbol_locations: set[space.Point] = set()
        self._numbers: list[Number] = []

        current_number: str = ""
        current_number_points: set[space.Point] = set()
        y: int
        line: str
        for y, line in enumerate(self.pi.as_list_of_strings()):
            line = line + "."  # Handle numbers at the end of the line.
            x: int
            char: str
            for x, char in enumerate(line):
                if char.isdigit():
                    current_number += char
                    current_number_points.add(space.Point(x, y))
                    continue
                if char == "*":
                    self._gear_locations.add(space.Point(x, y))
                if char != ".":
                    self._symbol_locations.add(space.Point(x, y))
                if current_number:
                    self._numbers.append(Number(int(current_number), current_number_points))
                    current_number = ""
                    current_number_points = set()

    def part_one(self) -> int:
        """Return the sum of the part numbers in the engine schematic."""
        result: int = 0
        symbol_neighbors: set[space.Point] = set()
        for point in self._symbol_locations:
            symbol_neighbors.update(set(point.neighbors_8(quadrant=4).values()))
        for number in self._numbers:
            if number.points.intersection(symbol_neighbors):
                result += number.number
        return result

    def part_two(self) -> int:
        """Return the sum of all the gear ratios in the engine schematic."""
        result: int = 0
        for gear_location in self._gear_locations:
            gear_neighbors: set[space.Point] = set(gear_location.neighbors_8(quadrant=4).values())
            gear_ratios: list[int] = []
            for number in self._numbers:
                if gear_neighbors.intersection(number.points):
                    gear_ratios.append(number.number)
                    continue
            if len(gear_ratios) == D03._GEAR_PART_COUNT:
                result += math.prod(gear_ratios)
        return result
