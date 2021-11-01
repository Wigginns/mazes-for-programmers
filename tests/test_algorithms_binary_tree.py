import pytest

from algorithms import BinaryTree
from algorithms.algorithm import Algorithm

#TODO: Come up with better tests than this
def test_binary_tree():
    b_t = BinaryTree()
    assert isinstance(b_t, BinaryTree)
    assert isinstance(b_t, Algorithm)