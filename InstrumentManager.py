__author__ = 'shgli'
import os
import pandas as pd
from exceptions import Exception
from ITradingComponent import ITradingComponent
from Calendar import Calendar


class InstrumentManager(ITradingComponent):
    def __init__(self,tradingContext,mappingDirectory):
        super(InstrumentManager,self).__init__(tradingContext)
        self.mappingDirectory = mappingDirectory
        self.futures = pd.DataFrame()

    def onBeginDay(self, tradingDay):
        mappingFileName = os.path.join(self.mappingDirectory, Calendar.dateToString(tradingDay) + '.mapping.csv')
        if not os.path.isfile(mappingFileName):
            raise Exception('can not open mapping file %s' % mappingFileName)
        self.futures = self.loadFromFile(mappingFileName)

    def onEndDay(self, tradingDay):
        pass

    def loadFromFile(self, mappingFileName):
        self.futures = pd.read_csv(mappingFileName, index_col='Name')
        self.futures['Product'] = self.futures.index.map(lambda name: name.split('_')[0])

    def getFuture(self, symbol):
        future = self.futures[symbol(self.futures)]
        if 1 <= len(future):
            return self.futures.ix[future.index[0]]
        else:
            return None

    def getFutures(self, filt=None):
        if filt is None:
            return self.futures
        else:
            return self.futures[filt(self.futures)]


if __name__ == '__main__':
    import nose
    import Symbol

    def setUp():
        global instrumentMgr
        instrumentMgr = InstrumentManager('day/meta')
        instrumentMgr.loadFromFile('~/20150605.mapping.csv')

    def tearDown():
        global instrumentMgr
        instrumentMgr = None

    def test_getFutre():
        global instrumentMgr
        future = instrumentMgr.getFuture(Symbol.Symbol('IF1506', 'CFFEX'))
        assert future is not None
        assert future.FeedCode == 'IF1506'
        assert future.Exchange == 'CFFEX'

    def test_getFutures():
        global instrumentMgr
        futures = instrumentMgr.getFutures(lambda instru: instru.Product == 'IF')
        assert futures is not None
        for future in futures.iterrows():
            assert future[1].Product == 'IF'

    nose.runmodule()
