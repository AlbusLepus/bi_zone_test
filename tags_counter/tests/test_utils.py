"""
Tests for tags_counter.processing module.
"""
from tags_counter.utils import count_elems


def test_count_elems():
    """ count_elems test1 """
    elems = ["a", "b", "a", "c", "z", "a", "c", "g", "fad", "1", 1]
    expected = {'a': 3, 'b': 1, 'c': 2, "z": 1, "g": 1, "fad": 1, "1": 1, 1: 1}
    assert count_elems(elems) == expected
    assert count_elems([]) == {}
