from qaamus2.models.basemodel import QaamusBaseModel


class MunawwirBerhubModel(QaamusBaseModel):

    def __init__(self, indo, arab, url):
        super(MunawwirBerhubModel, self).__init__(indo)

        self.indo = indo
        self.arab = arab
        self.url = url
