__author__ = 'shgli'
from EventFlow import EventFlow
from TimeBubble import TimeBuble
from TimeLine import TimeLine
from datetime import datetime
import Logger
class TradingContext(object):

    def __init__(self,fromDay, toDay):
        self.instrumentManager = None
        self.feedSource = None
        self.calendar = None

        self.timeLine = TimeLine()
        self.eventFlow = EventFlow()
        self.timeBubble = TimeBuble(self.timeLine)
        self.fromDay = fromDay
        self.toDay = toDay

    def check(self):
        if self.calendar is None:
            Logger.critical('calendar is None')
        if self.instrumentManager is None:
            Logger.critical("instrument manager is None")
        if self.feedSource is None:
            Logger.critical("feed source is None")

        self.fromDay = self.feedSource.feederCreator.adjustStartDay(self.fromDay)
        self.toDay = self.feedSource.feederCreator.adjustStartDay(self.toDay)
        if self.fromDay > self.toDay:
            Logger.critical('adjusted fromDay > adjusted toDay : (%s > %s)' % (self.fromDay.strftime('%Y%m%d'),self.toDay.strftime('%Y%m%d')))


    def run(self):
        self.check()

        self.instrumentManager.initialize()
        self.feedSource.initialize()


        runId = 1
        self.timeLine.tradingDay = self.calendar.getPreviousTradingDay(self.fromDay)

        while self.timeLine.tradingDay < self.toDay:
            tradingDay = self.calendar.getNextTradingDay(self.timeLine.tradingDay)
            self.timeLine.tradingDay = tradingDay
            self.timeLine.time = datetime(tradingDay.year, tradingDay.month, tradingDay.day)

            #emit onBeginDay event
            self.instrumentManager.onBeginDay(self.timeLine.tradingDay)
            self.feedSource.onBeginDay(self.timeLine.tradingDay)
            self.eventFlow.foreachNode(lambda node: node.onBeginDay(self.timeLine.tradingDay))

            while self.timeBubble.bubble():
                self.eventFlow.process(runId)

            #emit onEndDay event
            self.eventFlow.foreachNode(lambda node: node.onEndDay(self.timeLine.tradingDay))
            self.feedSource.onEndDay(self.timeLine.tradingDay)
            self.instrumentManager.onEndDay(self.timeLine.tradingDay)


