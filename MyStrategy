
from IStrategy import IStrategy
from Symbol import Symbol
class MyStrategy(IStrategy):

    def __init__(self,tradingContext):
        super(self,MyStrategy).__init__(tradingContext)

    def onBeginDay(self,tradingDay):
        self.ni = self.subscribe(Symbol('ni_01','SHFE'))

    def onEndDay(self,tradingDay):
        pass

