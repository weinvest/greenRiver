__author__ = 'shgli'

from ITradingComponent import ITradingComponent
class FeedSource(ITradingComponent):
    def __init__(self, feederCreator):
        self.feeders = {}
        self.feederCreator = feederCreator

    def subscribe(self,instrument):
        if not self.feeders.has_key(instrument.Name):
            feeder = self.feederCreator.create(instrument)
            feeder.initialize(self.tradingDay, self.getCurrentTradingSession())
            self.feeders[instrument.Name] = feeder

        return self.feeders[instrument.Name]


    def subscribeList(self,instruments):
        retFeeders = []
        for ix, instrument in instruments.iterrows():
            feeder = self.subscribe(instrument)
            if feeder is not None:
                retFeeders.append(feeder)
        return retFeeders

    def bubble(self):
        for instrument,feeder in self.feeders.iteritems():
            feeder.bubble()

    def onBeginDay(self,tradingDay):
        self.feeders = {}

    def onEndDay(self,tradingDay):
        pass