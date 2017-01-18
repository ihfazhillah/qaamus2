from qaamus2.models.munawwir import MunawwirModel
from qaamus2.models.munawwir_berhub_collections import MunawwirBerhubModelCollections
from nose import tools

BERHUBUNGAN = MunawwirBerhubModelCollections(x for x in range(3))
DATA = {'indo': 'makan',
        'arab': 'أكل',
        'baca': 'akala',
        'url': 'http://fakeurl.url',
        'berhubungan': BERHUBUNGAN}

def test_representation():
    munawwir = MunawwirModel(**DATA)
    expected = "<MunawwirModel -makan->"
    tools.eq_(expected, munawwir.__repr__())
