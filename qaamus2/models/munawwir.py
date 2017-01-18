"""Model munawwir"""
from qaamus2.models.basemodel import QaamusBaseModel
from qaamus2.models import munawwir_berhub_collections as mbc

class MunawwirModel(QaamusBaseModel):
    """Model Munawwir"""
    def __init__(self, indo, arab, baca, url, berhubungan):
        super(MunawwirModel, self).__init__(indo)
        self.indo = indo
        self.arab = arab
        self.baca = baca
        self.url = url
        self.berhubungan = self._validate_berhubungan(berhubungan)

    @classmethod
    def _validate_berhubungan(cls, berhubungan):
        if not isinstance(berhubungan, mbc.MunawwirBerhubModelCollections):
            raise ValueError(("berhubungan bukan isntance dari "
                              "MunawwirBerhubModelCollections"
                              "type(berhubungan) = %s" % type(berhubungan)))
        return berhubungan
