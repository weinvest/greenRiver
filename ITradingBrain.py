__author__ = 'shgli'
from ITradingComponent import ITradingComponent
from EventNode import EventNode
import EventType
class ITradingBrain(ITradingComponent, EventNode):

    def __init__(self, name, type, tradingContext):
        super(ITradingBrain, self).__init__(name, tradingContext)
        EventNode.__init__(self, name, type)
        self.__timer = []
        self.__marketData = []

    def subscribe(self,symbol):
        instrument = self.tradingContext.instrumentManager.getFuture(symbol)
        if instrument is None:
            return None

        return self.tradingContext.feedSource.subscribe(instrument)

    def onRaised(self,source):
        if EventType.FeedEvent == source.evtType:
            self.__marketData.append(source)
        elif EventType.TimerEvent == source.evtType:
            self.__timer.append(source)

    def onMarketData(self,data):
        pass

    def onTimer(self,timer):
        pass

    def doProcess(self, processId):
        hasEvent = False
        if 0 != len(self.__marketData):
            self.onMarketData(self.__marketData)
            self.__marketData = []
            hasEvent = True

        if 0 != len(self.__timer):
            for timer in self.__timer:
                self.onTimer(timer)
            self.__timer = []
            hasEvent = True
        return hasEvent