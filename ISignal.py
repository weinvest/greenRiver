__author__ = 'shgli'
from ITradingBrain import ITradingBrain
class ISignal(ITradingBrain):
    def initialize(self,tradingContext):
        super(ISignal,self).__init__(tradingContext)

