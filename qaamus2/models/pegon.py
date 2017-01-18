from qaamus2.models.basemodel import QaamusBaseModel


class PegonModel(QaamusBaseModel):
    """PegonModel"""

    def __init__(self, indo, arab, url):
        super(PegonModel, self).__init__(indo)

        self.indo = indo
        self.arab = arab
        self.url = url
