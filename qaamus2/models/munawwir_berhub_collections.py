from itertools import tee

class MunawwirBerhubModelCollections(object):
    
    def __init__(self, iterator):
        self.new, self.bak = tee(iterator)
        self.length = len(list(self.new))

    def __len__(self):
        return self.length

