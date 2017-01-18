from qaamus2.models.munawwir_berhub import MunawwirBerhubModel
from nose import tools

DATA = {'indo': 'mengambil tongkat',
        'arab': 'عَصِيَ',
        'url': 'http://qaamus.com/indonesia-arab/mengambil+tongkat/1'}

def test_representation():
    munawwir_berhub = MunawwirBerhubModel(**DATA)
    expected = '<MunawwirBerhubModel -mengambil tongkat->'
    tools.eq_(expected, munawwir_berhub.__repr__())


@tools.raises(ValueError)
def test_indo_tidak_boleh_integer():
    MunawwirBerhubModel(indo=123, arab='عربي', url='http://qaamus.com')

@tools.raises(ValueError)
def test_indo_tidak_boleh_string_digit():
    MunawwirBerhubModel(indo='123', arab='عربي', url='http://qaamus.com')
