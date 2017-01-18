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
        self.indo = self._check_angka(indo)
        self.arab = arab
        self.url = url
        super(AngkaModel, self).__init__(self.indo)

    @classmethod
    def _check_angka(cls, indo):
        """Angka harus berupa int, atau string angka"""
        if not isinstance(indo, int):
            raise ValueError(("Angka harus berupa int, "
                              "atau string berisi digit"))
        return indo
