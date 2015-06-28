__author__ = 'shgli'
from EventFlow import EventFlow
from TimeBubble import TimeBuble
from TimeLine import TimeLine
import Logger
class TradingContext(object):

    def __init__(self,fromDay, toDay):
        self.instrumentManager = None
        self.feedSource = None
        self.calendar = None

        self._eventFlow = EventFlow()
        self._timeBubble = TimeBuble()
        self.fromDay = fromDay
        self.toDay = toDay
        self.timeLine = TimeLine()

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
        self._eventFlow.foreachNode(lambda node: node.onBeginDay(self.timeLine.tradingDay))

        while self.timeLine.tradingDay < self.toDay:
            self.timeLine.tradingDay = self.calendar.getNextTradingDay(self.timeLine.tradingDay)

            self._timeBubble.


            self._timeBubble.process(runId)
            self._eventFlow.process(runId)

            self._eventFlow.foreachNode(lambda node: node.onEndDay(self.timeLine.tradingDay))


