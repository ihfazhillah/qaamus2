from qaamus2.models.pegon import PegonModel
from nose import tools


DATA = {'indo': 'tongkat',
        'arab': ' تونغكات',
        'url': 'http://qaamus.com/terjemah-nama/tongkat'}

def test_representation():
    pegon = PegonModel(**DATA)
    expected = '<PegonModel -tongkat->'
    tools.eq_(expected, pegon.__repr__())
