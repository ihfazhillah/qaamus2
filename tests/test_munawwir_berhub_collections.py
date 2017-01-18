from qaamus2.models.munawwir_berhub_collections import MunawwirBerhubModelCollections
from nose import tools


DATA = (x for x in range(5))

def test_length():
    x = MunawwirBerhubModelCollections(DATA)
    expected = 5
    tools.eq_(expected, len(x))
