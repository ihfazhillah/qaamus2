from qaamus2.models.basemodel import QaamusBaseModel


class AngkaModel(QaamusBaseModel):

    def __init__(self, indo, arab, url):
        self.indo = indo
        self.arab = arab
        self.url = url
