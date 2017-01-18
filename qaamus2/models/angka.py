"""Angka model modul"""
from qaamus2.models.basemodel import QaamusBaseModel


class AngkaModel(QaamusBaseModel):
    """Merepresentasikan angka model,

    params:
        - indo : indonesia
        - arab : arab
        - url : url pencarian
    """

    def __init__(self, indo, arab, url):
        self.indo = indo
        self.arab = arab
        self.url = url
        super(AngkaModel, self).__init__(self.indo)
