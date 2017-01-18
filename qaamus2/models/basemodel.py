class QaamusBaseModel(object):

    def __init__(self, indo, *args, **kwargs):
        self.indo = indo

    def __repr__(self):
        return '<%s -%s->' % (self.__class__.__name__,
                              self.indo)
