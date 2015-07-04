__author__ = 'shgli'
import Logger
from ITradingComponent import ITradingComponent
class FeedSource(ITradingComponent):
    def __init__(self, tradingContext, feederCreator):
        super(FeedSource,self).__init__('FeedSource', tradingContext)

        if feederCreator is None:
            Logger.critical("feed creator is None")

        self.feeders = {}
        self.feederCreator = feederCreator


    def initialize(self):
        pass

    def subscribe(self,instrument):
        if not self.feeders.has_key(instrument.Name):
            feeder = self.feederCreator.create(instrument,self.timeLine)
            feeder.initialize(self.tradingDay, self.getCurrentTradingSession())
            self.feeders[instrument.Name] = feeder
            self.addTask(feeder)
        return self.feeders[instrument.Name]


    def subscribeList(self,instruments):
        retFeeders = []
        for ix, instrument in instruments.iterrows():
            feeder = self.subscribe(instrument)
            if feeder is not None:
                retFeeders.append(feeder)
        return retFeeders

    def onBeginDay(self,tradingDay):
        self.feeders = {}

    def onEndDay(self,tradingDay):
        pass