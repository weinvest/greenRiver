__author__ = 'shgli'
from ITradingComponent import ITradingComponent

class TradingBrain(ITradingComponent):

    def __init__(self,tradingContext):
        self.tradingContext = tradingContext

    def subscribe(self,symbol):
        instrument = self.tradingContext.instrumentManager.getFuture(symbol)
        if instrument is None:
            return None

        return self.tradingContext.feedSource.subscribe(instrument)