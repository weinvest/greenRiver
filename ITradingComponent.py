__author__ = 'shgli'

class ITradingComponent(object):

    def __init__(self):
        self.mCurrentTradingSession = None

    def onBeginDay(self,tradingDay):
        pass

    def onEndDay(self,tradingDay):
        pass

    def onTradingSessionChange(self,fromSession,toSession):
        pass

    def initialize(self):
        pass

    def getCurrentTradingSession(self):
        return self.mCurrentTradingSession



