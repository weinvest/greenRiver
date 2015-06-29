__author__ = 'shgli'
from ITradingBrain import TradingBrain
class ISignal(TradingBrain):
    def initialize(self,tradingContext):
        super(ISignal,self).__init__(tradingContext)

