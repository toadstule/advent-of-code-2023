"""Test day 3."""
import os

import pytest

from aoc import d03


@pytest.mark.skipif(os.getenv("TEST_DAY") not in (None, "3"), reason="Not today")
def test__d03_part_one() -> None:
    """Test part one."""
    assert d03.D03(filename="d03_pre1.txt").part_one() == 4361
    assert d03.D03(filename="d03.txt").part_one() == 554003


@pytest.mark.skipif(os.getenv("TEST_DAY") not in (None, "3"), reason="Not today")
def test__d03_part_two() -> None:
    """Test part two."""
    assert d03.D03(filename="d03_pre1.txt").part_two() == 467835
    assert d03.D03(filename="d03.txt").part_two() == 87263515
