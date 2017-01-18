"""Munawwir berhubungan model"""
from qaamus2.models.basemodel import QaamusBaseModel


class MunawwirBerhubModel(QaamusBaseModel):
    """Class MunawwirBerhubModel"""

    def __init__(self, indo, arab, url):
        super(MunawwirBerhubModel, self).__init__(indo)

        self.indo = self._validate_indo(indo)
        self.arab = arab
        self.url = url

    @classmethod
    def _validate_indo(cls, indo):
        if isinstance(indo, int) or indo.isdigit():
            raise ValueError("indo tidak boleh integer")

        return indo
