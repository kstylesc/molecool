"""
Unit and regression test for the molecool package.
"""

# Import package, test suite, and other packages as needed
import molecool
import pytest
import sys
import numpy as np


def test_molecool_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "molecool" in sys.modules


def test_calculate_distance():
    """Test that calculate_disntances calculates what we expected"""

    r1 = np.array([0, 0, 0])
    r2 = np.array([0, 1, 0])

    expected_distance = 1

    calculated_distance = molecool.calculate_distance(r1, r2)

    assert expected_distance == calculated_distance


def test_calculate_angle():
    """Test that calculate_disntances calculates what we expected"""

    r1 = np.array([0, 0, -1])
    r2 = np.array([0, 0, 0])
    r3 = np.array([1, 0, 0])

    expected_angle = np.pi / 2

    calculated_angle = molecool.calculate_angle(r1, r2, r3)

    assert expected_angle == calculated_angle

    r1 = np.array([0, 0, -1])
    r2 = np.array([0, 1, 0])
    r3 = np.array([1, 0, 0])

    expected_angle = np.pi / 3

    calculated_angle = molecool.calculate_angle(r1, r2, r3)

    assert np.allclose(expected_angle, calculated_angle)


@pytest.mark.parametrize(
    "r1, r2, r3, expected_angle",
    [
        (np.array([1, 0, 0]), np.array([0, 0, 0]), np.array([0, 1, 0]), 90),
        (np.array([0, 0, -1]), np.array([0, 1, 0]), np.array([1, 0, 0]), 60),
    ],
)
def test_calculate_angle_many(r1, r2, r3, expected_angle):
    calculated_angle = molecool.calculate_angle(r1, r2, r3, degrees=True)
    assert pytest.approx(calculated_angle) == expected_angle
