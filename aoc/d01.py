"""Advent of Code 2022 -- Day 1: Trebuchet?!.

Reference: https://adventofcode.com/2023/day/1
"""
from typing import Final, Optional

from jibaoc import solver


class D01(solver.Solver):
    """Solve puzzle for day 1."""

    _TEXT_DIGITS: Final[dict[int, str]] = {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
    }
    _REVERSE_TEXT_DIGITS: Final[dict[int, str]] = {
        k: "".join(reversed(v)) for k, v in _TEXT_DIGITS.items()
    }

    def __post_init__(self) -> None:
        """Initialize a D01 instance."""
        self._calibration_doc = self.pi.as_list_of_strings()

    def part_one(self) -> int:
        """Return the sum of all the calibration values."""
        return self._get_calibration_value(include_text_digits=False)

    def part_two(self) -> int:
        """Return the sum of all the calibration values; include text-represented digits."""
        return self._get_calibration_value(include_text_digits=True)

    def _get_calibration_value(self, include_text_digits: bool) -> int:
        """Return the calibration value from the calibration doc."""
        return sum(
            self._get_first_digit(line, include_text_digits) * 10
            + self._get_last_digit(line, include_text_digits)
            for line in self._calibration_doc
        )

    def _get_first_digit(self, line: str, include_text_digits: bool = False) -> int:
        """Return the first digit in the given string, times 10."""
        return self._get_digit(
            line=line, text_digits=D01._TEXT_DIGITS if include_text_digits else None
        )

    def _get_last_digit(self, line: str, include_text_digits: bool = False) -> int:
        """Return the last digit in the given string."""
        return self._get_digit(
            line="".join(reversed(line)),
            text_digits=D01._REVERSE_TEXT_DIGITS if include_text_digits else None,
        )

    @staticmethod
    def _get_digit(line: str, text_digits: Optional[dict[int, str]]) -> int:
        """Return the first digit in the given string, optionally using given text_digits."""
        for i, char in enumerate(line):
            if char.isdigit():
                return int(char)
            if text_digits:
                for digit, text in text_digits.items():
                    if line[i:].startswith(text):
                        return digit
        raise ValueError("Unable to find digit in line")
