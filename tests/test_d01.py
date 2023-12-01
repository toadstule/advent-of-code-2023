"""Test day 1."""
import os

import pytest

from aoc import d01


@pytest.mark.skipif(os.getenv("TEST_DAY") not in (None, "1"), reason="Not today")
def test__d01_part_one() -> None:
    """Test part one."""
    assert d01.D01(filename="d01_pre1.txt").part_one() == 142
    assert d01.D01(filename="d01.txt").part_one() == 56465


@pytest.mark.skipif(os.getenv("TEST_DAY") not in (None, "1"), reason="Not today")
def test__d01_part_two() -> None:
    """Test part two."""
    assert d01.D01(filename="d01_pre2.txt").part_two() == 281
    assert d01.D01(filename="d01.txt").part_two() == 55902
