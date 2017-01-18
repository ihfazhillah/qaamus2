from qaamus2.models.basemodel import QaamusBaseModel


class PegonModel(QaamusBaseModel):
    """PegonModel"""

    def __init__(self, indo, arab, url):
        super(PegonModel, self).__init__(indo)

        self.indo = self._validate_indo(indo)
        self.arab = arab
        self.url = url

    @classmethod
    def _validate_indo(cls, indo):
        """Validasi indo, tidak bole berupa int atau
        string berisi digit"""

        if isinstance(indo, int) or indo.isdigit():
            raise ValueError("""Value param indo tidak bole berisi int,
                                atau string berisi digit""")
        return indo
