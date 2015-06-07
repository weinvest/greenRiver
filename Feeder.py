
from EventNode import EventNode
import pandas as pd
class Feeder(EventNode):
    def __init__(self,instrument):
        self.instrument = instrument

    def onBeginDay(self,tradingDay):
        self.marketDatas = pd.read_table()
    def doProcess(self, processId):
        pass