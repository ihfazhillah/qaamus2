from qaamus2.models.munawwir_berhub import MunawwirBerhubModel
from nose import tools

DATA = {'indo': 'mengambil tongkat',
        'arab': 'عَصِيَ',
        'url': 'http://qaamus.com/indonesia-arab/mengambil+tongkat/1'}

def test_representation():
    munawwir_berhub = MunawwirBerhubModel(**DATA)
    expected = '<MunawwirBerhubModel -mengambil tongkat->'
    tools.eq_(expected, munawwir_berhub.__repr__())
