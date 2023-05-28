class Stock(object):
    def __init__(self, symbol, **kwargs):
        self.__dict__.update(kwargs)
        self.symbol = symbol

