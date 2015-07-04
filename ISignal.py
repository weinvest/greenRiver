__author__ = 'shgli'
from ITradingBrain import ITradingBrain
import EventType
class ISignal(ITradingBrain):
    def initialize(self, name, tradingContext):
        super(ISignal, self).__init__(name, EventType.SignalEvent, tradingContext)

