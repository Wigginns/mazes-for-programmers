import pytest
import sys
sys.path.append('../package')

from package.cell import Cell

def test_Cell_instantiation():
    assert Cell(1,2)