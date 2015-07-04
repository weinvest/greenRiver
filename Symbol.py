__author__ = 'shgli'

class Symbol(object):
    def __init__(self,feedCode,exchange):
        self.feedCode = feedCode
        self.exchange = exchange
        self.isName = -1 != self.feedCode.find('_')

    def __call__(self, *args, **kwargs):
        instrument = args[0]
        if self.isName:
            return self.feedCode == instrument.Name
        return (self.feedCode == instrument.FeedCode) & (self.exchange == instrument.Exchange)