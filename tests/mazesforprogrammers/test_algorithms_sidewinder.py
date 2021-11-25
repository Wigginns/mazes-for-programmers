from mazesforprogrammers import Sidewinder, Algorithm


# TODO: Come up with better tests than this
def test_sidewinder():
    sw = Sidewinder()
    assert isinstance(sw, Sidewinder)
    assert isinstance(sw, Algorithm)
