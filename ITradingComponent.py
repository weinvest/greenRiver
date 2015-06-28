__author__ = 'shgli'

class ITradingComponent(object):

    def __init__(self):
        self.currentTradingSession = None
        self.tradingDay = None

    def onBeginDay(self, tradingDay):
        self.tradingDay = tradingDay

    def onEndDay(self, tradingDay):
        pass

    def onTradingSessionChange(self,fromSession,toSession):
        self.currentTradingSession = toSession

    def initialize(self):
        pass

    def getTradingDay(self):
        return self.tradingDay

    def getCurrentTradingSession(self):
        return self.currentTradingSession



