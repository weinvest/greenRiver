__author__ = 'shgli'
from InstrumentManager import InstrumentManager
from FeedSource import  FeedSource
from LocalFeederCreator import LocalFeederCreator
from TradingContext import TradingContext
from Calendar import Calendar
from ISignal import ISignal
from Symbol import Symbol
import argparse
import sys
import os

class OutputMarket(ISignal):
    def __init__(self, tradingContext, symbol):
        super(OutputMarket, self).__init__('Output', tradingContext)
        self.symbol = symbol


    def onBeginDay(self, tradingDay):
        self.feeder = self.subscribe(self.symbol)
        print('Bid1Price,Bid1Qty,Ask1Qty,Ask1Price')

    def onMarketData(self,dates):
        print('%lf,%d,%d,%lf' %(self.feeder.getBidPrice(0),self.feeder.getBidQty(0),self.feeder.getAskQty(0),self.feeder.getAskPrice(0)))

    def onEndDay(self, tradingDay):
        self.feeder.data.LastPrice.plot()

if __name__ == '__main__':
    scriptPath,greenRiver = os.path.split(os.path.abspath(sys.argv[0]))

    parser = argparse.ArgumentParser(prog=greenRiver
        ,description = " generate tailsignal configure")

    parser.add_argument('-m','--mappingRoot',help='directory that contains mapping files')
    parser.add_argument('-d','--dataRoot',help='direcotry that contains data')
    parser.add_argument('-o','--holidayFile',help='holiday file')
    parser.add_argument('-f','--fromDay',help='backtest from this day')
    parser.add_argument('-t','--toDay',help='backtest to this day')
    args = parser.parse_args()


    tradingContext = TradingContext()
    tradingContext.instrumentManager = InstrumentManager(tradingContext,args.mappingRoot)
    tradingContext.feedSource = FeedSource(tradingContext,LocalFeederCreator(args.dataRoot))
    tradingContext.calendar = Calendar(open(args.holidayFile, 'r'))

    tradingContext.initialize(Calendar.dateFromString(args.fromDay),Calendar.dateFromString(args.toDay))

    outSignal = OutputMarket(tradingContext, Symbol('IF_01','CFFEX'))

    tradingContext.run()


