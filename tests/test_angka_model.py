from qaamus2.models.angka import AngkaModel
from nose import tools

DATA = {'indo': 12,
        'arab': 'اثنا عشر',
        'url': 'http://coba.saja/angka/12'}

def test_angka_model_representation():
    angka = AngkaModel(**DATA)
    expected = '<AngkaModel -12->'
    tools.eq_(expected, angka.__repr__())

def test_data_harus_betul():
    angka = AngkaModel(**DATA)
    tools.eq_(12, angka.indo)
    tools.eq_("اثنا عشر", angka.arab)
    tools.eq_("http://coba.saja/angka/12", angka.url)

@tools.raises(ValueError)
def test_raise_value_error_kalau_angka_bukan_digit_atau_string_angka():
    angka = AngkaModel(indo='inistring', arab='ini string',
                       url='ini url')

def test_indo_string_berisi_digit_tidak_raise_valueerror():
    angka = AngkaModel('12', 'عربي', 'url')
