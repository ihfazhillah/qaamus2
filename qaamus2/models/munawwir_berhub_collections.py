from itertools import tee

class MunawwirBerhubModelCollections(object):
    
    def __init__(self, iterator):
        iterator = iter(iterator)
        self.new, self.bak = tee(iterator)
        self.length = len(list(self.bak))

    def __len__(self):
        return self.length

    def __iter__(self):
        return self.new

