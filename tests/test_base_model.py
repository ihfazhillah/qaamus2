from qaamus2.models.basemodel import QaamusBaseModel
from nose import tools

def test_base_model_repr():
    base = QaamusBaseModel('ini base')
    expected = '<QaamusBaseModel -ini base->'
    tools.eq_(expected, base.__repr__())
