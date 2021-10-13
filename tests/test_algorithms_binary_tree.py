import pytest

from algorithms import BinaryTree
from algorithms.algorithm import Algorithm

def test_binary_tree():
    b_t = BinaryTree()
    assert isinstance(b_t, BinaryTree)
    assert isinstance(b_t, Algorithm)