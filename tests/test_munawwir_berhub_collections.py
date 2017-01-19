from qaamus2.models.munawwir_berhub_collections import MunawwirBerhubModelCollections
from nose import tools
# from copy import copy

DATA = [x for x in range(5)]

def test_length():
    x = MunawwirBerhubModelCollections(DATA)
    expected = 5
    tools.eq_(expected, len(x))

def test_returned():
    x = MunawwirBerhubModelCollections(DATA)
    expected = [x for x in range(5)]
    tools.eq_(expected, list(x))

# bug tidak bisa menggunakan next
def test_next():
    x = MunawwirBerhubModelCollections(DATA)
    expected = 0
    tools.eq_(expected, next(x))
