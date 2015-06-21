__author__ = 'shgli'
from EventFlow import EventFlow
from TimeBubble import TimeBuble
class TradingContext(object):

    def __init__(self,fromTime,toTime):
        self.instrumentManager = None
        self.feedSource = None
        self._eventFlow = EventFlow()
        self._timeBubble = TimeBuble()
        self.fromTime = fromTime
        self.toTime = toTime

    def run(self):
        runId = 1
        self._timeBubble.process(runId)
        self._eventFlow.process(runId)


