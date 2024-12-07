from unittest.mock import patch
from day1.similarityScore import similarityScore


def test_totalDistance():
    with patch("sys.argv", ["", "test_list.txt"]):
        assert 31 == similarityScore.similarity_score()
    with patch("sys.argv", ["", "lists.txt"]):
        assert 21790168 == similarityScore.similarity_score()
