from qaamus2.models.pegon import PegonModel
from nose import tools


DATA = {'indo': 'tongkat',
        'arab': ' تونغكات',
        'url': 'http://qaamus.com/terjemah-nama/tongkat'}

def test_representation():
    pegon = PegonModel(**DATA)
    expected = '<PegonModel -tongkat->'
    tools.eq_(expected, pegon.__repr__())

@tools.raises(ValueError)
def test_raise_value_error_ketika_dimasukkan_integer():
    pegon = PegonModel(indo=12, arab='عربي', url='http://qaamus.com')
