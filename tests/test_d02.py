"""Test day 2."""
import os

import pytest

from aoc import d02


@pytest.mark.skipif(os.getenv("TEST_DAY") not in (None, "2"), reason="Not today")
def test__d02_part_one() -> None:
    """Test part one."""
    assert d02.D02(filename="d02_pre1.txt").part_one() == 8
    assert d02.D02(filename="d02.txt").part_one() == 2156


@pytest.mark.skipif(os.getenv("TEST_DAY") not in (None, "2"), reason="Not today")
def test__d02_part_two() -> None:
    """Test part two."""
    assert d02.D02(filename="d02_pre1.txt").part_two() == 2286
    assert d02.D02(filename="d02.txt").part_two() == 66909
