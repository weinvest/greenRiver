__author__ = 'shgli'
from ISignal import ISignal
from FeedLevel import FeedLevel

class MySignal(ISignal):
    def __init__(self, symbol,maxLevel):
        super(MySignal, self).__init__()
        self.symbol = symbol
        self.maxLevel = maxLevel
        self.bids = []
        self.asks = []

    def onBeginDay(self):
        self.feeder = self.subscribeSymbol(self.symbol)

    def onMarketData(self,dates):
        self.updateBids(self.feeder.bid1Price,self.feeder.bid1Qty)
        self.updateAsks(self.feeder.ask1Price,self.feeeder.bid1Qty)

    def updateBids(self,price,qty):
        tickPrice = round(price / self.feeder.instrument.tickSize)
        self.bids = [level for level in self.bids if level.tickPrice < tickPrice]
        self.bids.append(FeedLevel(price,qty,tickPrice))

    def updateAsks(self,price,qty):
        tickPrice = round(price / self.feeder.instrument.tickSize)
        self.asks = [level for level in self.asks if level.tickPrice > tickPrice]
        self.asks.append(FeedLevel(price,qty,tickPrice))





