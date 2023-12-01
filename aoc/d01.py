"""Advent of Code 2022 -- Day 1: DAY_TITLE.

Reference: https://adventofcode.com/2022/day/1
"""  # Trebuchet?!
from jibaoc import solver


class D01(solver.Solver):
    """Solve puzzle for day 1."""

    def __post_init__(self) -> None:
        """Initialize a D01 instance."""
        self._calibration_doc = self.pi.as_list_of_strings()

    def part_one(self) -> int:
        """Return the sum of all the calibration values."""
        result: int = 0
        for line in self._calibration_doc:
            digits: list[str] = [x for x in line if x.isdigit()]
            result += int(digits[0]) * 10 + int(digits[-1])
        return result

    def part_two(self) -> int:
        """Return the sum of all the calibration values."""
        text_digits: dict[int, str] = {
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
        result: int = 0
        for line in self._calibration_doc:
            first_digit: int = 0
            last_digit: int = 0
            for i, char in enumerate(line):
                if char.isdigit():
                    first_digit = int(char)
                    break
                for digit, text in text_digits.items():
                    if line[i:].startswith(text):
                        first_digit = digit
                        break
                if first_digit:
                    break
            for i, char in reversed(list(enumerate(line))):
                if char.isdigit():
                    last_digit = int(char)
                    break
                for digit, text in text_digits.items():
                    if line[i - 1 :].startswith(text):
                        last_digit = digit
                        break
                if last_digit:
                    break
            result += first_digit * 10 + last_digit
        return result
