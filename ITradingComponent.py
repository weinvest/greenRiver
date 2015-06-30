__author__ = 'shgli'
from EventNode import EventNode
class ITradingComponent(EventNode):

    def __init__(self,name,type,tradingContext):
        super(ITradingComponent,self).__init__(name,type)
        self.currentTradingSession = None
        self.tradingContext = tradingContext

    def onBeginDay(self, tradingDay):
        pass

    def onEndDay(self, tradingDay):
        pass

    def onTradingSessionChange(self,fromSession,toSession):
        self.currentTradingSession = toSession

    def initialize(self):
        pass

    def getTradingDay(self):
        return self.tradingContext.timeLine.tradingDay

    def getTime(self):
        return self.tradingContext.timeLine.time

    def getCurrentTradingSession(self):
        return self.currentTradingSession

    def addTask(self,task):
        self.tradingContext.timeBubble.add(task)

    def doProcess(self, processId):
        pass


