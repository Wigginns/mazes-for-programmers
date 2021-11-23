import pytest

from mazesforprogrammers import Sidewinder, Algorithm

#TODO: Come up with better tests than this
def test_binary_tree():
    sw = Sidewinder()
    assert isinstance(sw, Sidewinder)
    assert isinstance(sw, Algorithm)