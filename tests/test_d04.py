"""Test day 4."""
import os

import pytest

from aoc import d04


@pytest.mark.skipif(os.getenv("TEST_DAY") not in (None, "4"), reason="Not today")
def test__d04_part_one() -> None:
    """Test part one."""
    assert d04.D04(filename="d04_pre1.txt").part_one() == 13
    assert d04.D04(filename="d04.txt").part_one() == 21105


@pytest.mark.skipif(os.getenv("TEST_DAY") not in (None, "4"), reason="Not today")
def test__d04_part_two() -> None:
    """Test part two."""
    assert d04.D04(filename="d04_pre1.txt").part_two() == 30
    assert d04.D04(filename="d04.txt").part_two() == 5329815
