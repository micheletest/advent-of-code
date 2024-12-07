from unittest.mock import patch
from day1.totalDistance import totalDistance


def test_totalDistance():
    with patch("sys.argv", ["", "test_list.txt"]):
        assert 11 == totalDistance.total_distance()
    with patch("sys.argv", ["", "lists.txt"]):
        assert 1151792 == totalDistance.total_distance()
