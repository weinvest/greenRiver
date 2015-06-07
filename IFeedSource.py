__author__ = 'shgli'

from ITradingComponent import ITradingComponent
class IFeedSource(ITradingComponent):
    def __init__(self):
        self.instruments = []
        self.feeders = []


    def subscribe(self,instrument):
        self.instruments.append(instrument)

    def subscribeList(self,instruments):
        self.instruments.extend(instruments)

    def onBeginDay(self,tradingDay):
