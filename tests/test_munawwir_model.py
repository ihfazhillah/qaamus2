from qaamus2.models.munawwir import MunawwirModel
from qaamus2.models.munawwir_berhub_collections import MunawwirBerhubModelCollections
from nose import tools

BERHUBUNGAN = MunawwirBerhubModelCollections(x for x in range(3))
DATA = {'indo': 'makan',
        'arab': 'أكل',
        'baca': 'akala',
        'url': 'http://fakeurl.url',
        'sumber': 'sumber',
        'berhubungan': BERHUBUNGAN}

def test_representation():
    munawwir = MunawwirModel(**DATA)
    expected = "<MunawwirModel -makan->"
    tools.eq_(expected, munawwir.__repr__())

@tools.raises(ValueError)
def test_berhubungan_harus_instance_dari_munawwirberhubmodelcollections():
    data = DATA.copy()
    data['berhubungan'] = 'apasaja'
    MunawwirModel(**data)

def test_munawwir_tanpa_baca():
    data = DATA.copy()
    del data['baca']

    #: pastikan tidak ada exception disini
    munawwir = MunawwirModel(**data)

    tools.eq_(munawwir.indo, 'makan')
