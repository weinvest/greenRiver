__author__ = 'shgli'

class Symbol(object):
    def __init__(self,feedCode,exchange):
        self.feedCode = feedCode
        self.exchange = exchange

    def __call__(self, *args, **kwargs):
        instrument = args[0]
        return (self.feedCode == instrument.FeedCode) & (self.exchange == instrument.Exchange)