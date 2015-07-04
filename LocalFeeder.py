
from EventNode import EventNode
import pandas as pd
import os
from os import path
from IFeeder import IFeeder
from Float import Float
from dateutil.parser import parse

class LocalFeeder(IFeeder):
    def __init__(self, instrument, timeLine, dataPath):
        super(LocalFeeder, self).__init__(instrument.Name,timeLine)

        self.instrument = instrument
        self.dataPath = dataPath
        self.columns = ["Recivetime","LastPrice","LastQty","Bid1Price","Bid1Qty",
                        "Ask1Price","Ask1Qty","Bid2Price", "Bid2Qty","Ask2Price",
                        "Ask2Qty","Bid3Price","Bid3Qty","Ask3Price","Ask3Qty",
                        "Bid4Price","Bid4Qty","Ask4Price","Ask4Qty","Bid5Price",
                        "Bid5Qty","Ask5Price","Ask5Qty","TotalQty","AveragePrice",
                        "OpenPrice","HighestPrice","LowestPrice","ClosePrice","PrevClosePrice",
                        "SettlementPrice","PrevSettlementPrice","OpenInterest","PrevInterest",
                        "Turnover","LowerLimit","UpperLimit","CurrentDelta","PrevDelta",
                        "FeedPhase"]
        self.data = None
        self.currentRow = None
        self.currentLoc = -1
        self.nextLoc = 0

    def initialize(self,tradingSession):
        tradingDay = self.timeLine.tradingDay
        dataFileName = self.getDataFileName(tradingDay, tradingSession)
        dataFilePath = path.join(self.getDataDirectory(tradingDay, tradingSession), dataFileName)
        repTradingDay = tradingDay.strftime('%Y%m%d')
        if not path.exists(dataFilePath):
            compressFileName = path.join(self.getDataDirectory(tradingDay, tradingSession)
                                         , repTradingDay + '.tar.bz2')
            if path.exists(compressFileName):
                import tarfile
                tmpRoot = path.join('/tmp/', tradingSession.name)
                tmpDirectory = path.join(tmpRoot, repTradingDay)
                if not path.exists(tmpDirectory):
                    os.makedirs(tmpDirectory)

                dataFilePath = path.join(tmpDirectory, dataFileName)
                if not path.exists(dataFilePath):
                    compressFile = tarfile.open(compressFileName,'r:bz2')
                    compressFile.extract(path.join(repTradingDay,dataFileName), tmpRoot)
        self.data = pd.read_csv(dataFilePath
                                , parse_dates=True
                                , skiprows=2
                                , delimiter='\s+'
                                , index_col=0
                                , names=self.columns
                                , date_parser = lambda x : parse(repTradingDay + ' ' + x)
                                )
        self.data.LastQty = self.data.TotalQty - self.data.TotalQty.shift(1)

        self.nextLoc = self.data.index.searchsorted(self.timeLine.time,side='right')
        self.currentLoc = self.nextLoc - 1

    def getDataFileName(self,tradingDay,tradingSession):
        return self.instrument.FeedCode + tradingDay.strftime('_%Y%m%d.txt')

    def getDataDirectory(self,tradingDay, tradingSession):
        subDir = path.join(self.dataPath, 'day')
        if tradingSession.name == 'NIGHT':
            subDir = path.join(self.dataPath, 'night')

        return path.join(subDir,tradingDay.strftime('%Y'), tradingDay.strftime('%Y%m'), tradingDay.strftime('%Y%m%d'))

    def getMidPrice(self):
        bestBidPrice = self.getBidPrice(0)
        bestAskPrice = self.getAskPrice(0)
        if bestBidPrice is not Float.nan and bestAskPrice is not Float.nan:
            return (bestBidPrice + bestAskPrice) / 2
        elif bestBidPrice is not Float.nan:
            return bestBidPrice
        elif bestAskPrice is not Float.nan:
            return bestAskPrice
        else:
            return Float.nan

    def _getAttrFromCurrentRow(self,attrName,defaultValue):
        if self.currentRow is None:
            return defaultValue
        else:
            return getattr(self.currentRow,attrName)

    def getBidPrice(self, level):
        return self._getAttrFromCurrentRow('Bid%dPrice' % (level + 1), Float.nan)

    def getBidQty(self, level):
        return self._getAttrFromCurrentRow('Bid%dQty' % (level + 1), 0)

    def getAskPrice(self, level):
        return self._getAttrFromCurrentRow('Ask%dPrice' % (level + 1), Float.nan)

    def getAskQty(self, level):
        return self._getAttrFromCurrentRow('Ask%dQty' % (level + 1), 0)

    def getLastPrice(self, level):
        return self._getAttrFromCurrentRow('LastPrice', Float.nan)

    def getLastQty(self, level):
        return self._getAttrFromCurrentRow('LastQty', 0)

    def getUpperLimit(self):
        return self._getAttrFromCurrentRow('UpperLimit', Float.max)

    def getLowerLimit(self):
        return self._getAttrFromCurrentRow('LowerLimit', 0)

    def getPrevClose(self):
        return self._getAttrFromCurrentRow('PrevClosePrice', Float.nan)

    def getPrevSettlement(self):
        return self._getAttrFromCurrentRow('PrevSettlementPrice', Float.nan)

    def getOpenInterest(self):
        return self._getAttrFromCurrentRow('OpenInterest', 0)

    def getNextTime(self):
        if self.nextLoc >= len(self.data.index):
            return None
        return self.data.index[self.nextLoc]

    def bubble(self):
        self.currentLoc = self.nextLoc
        self.nextLoc += 1
        self.raiseSelf()
        return True

    def doProcess(self, processId):
        self.currentRow = self.data.iloc[self.currentLoc]
        return True


if __name__ == '__main__':
    import nose
    from Calendar import Calendar
    from datetime import datetime
    from Dict import Dict

    def test_initialize():
        instrument = Dict(Name = 'IF_01',FeedCode='IF1509')
        feeder = LocalFeeder(instrument,Dict(tradingDay = Calendar.dateFromInt(20150629),time=datetime.strptime('20150629 09:20:00.000','%Y%m%d %H:%M:%S.%f')),'/home/shgli/data')
        feeder.initialize(Dict(name='AM'))
        print feeder.data.Ask1Price
        assert feeder.data

    def test_bubble():
        pass

    nose.runmodule()