__author__ = 'shgli'
from EventNode import EventNode
from TimeTask import TimeTask
import EventType
class IFeeder(EventNode,TimeTask):
    def __init__(self,name,timeLine):
        EventNode.__init__(self, name, EventType.FeedEvent)
        self.timeLine = timeLine

    def getMidPrice(self):
        pass

    def getBidPrice(self, level):
        pass

    def getBidQty(self, level):
        pass

    def getAskPrice(self, level):
        pass

    def getAskQty(self, level):
        pass

    def getLastPrice(self, level):
        pass

    def getLastQty(self, level):
        pass

    def getUpperLimit(self):
        pass

    def getLowerLimit(self):
        pass

    def getPrevClose(self):
        pass

    def getPrevSettlement(self):
        pass

    def getOpenInterest(self):
        pass

    def getBidBookOrderQty(self,level,rank):
        return 0

    def getAskBookOrderQty(self,level,rank):
        return 0