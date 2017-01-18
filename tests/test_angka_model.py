from qaamus2.models.angka import AngkaModel
from nose import tools

DATA = {'indo': 12,
        'arab': 'اثنا عشر',
        'url': 'http://coba.saja/angka/12'}

def test_angka_model_representation():
    angka = AngkaModel(**DATA)
    expected = '<AngkaModel -12->'
    tools.eq_(expected, angka.__repr__())
