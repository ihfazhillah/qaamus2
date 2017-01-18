from qaamus2.models.basemodel import QaamusBaseModel


class MunawwirModel(QaamusBaseModel):
    def __init__(self, indo, arab, baca, url, berhubungan):
        super(MunawwirModel, self).__init__(indo)
        self.indo = indo
        self.arab = arab
        self.baca = baca
        self.url = url
        self.berhubungan = berhubungan
