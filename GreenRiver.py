__author__ = 'shgli'
from InstrumentManager import InstrumentManager
from FeedSource import  FeedSource
from LocalFeederCreator import LocalFeederCreator
from TradingContext import TradingContext
from Calendar import Calendar
import argparse
import sys
import os

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
    tradingContext.calendar = Calendar(open(args.holidayFile,'r'))

    tradingContext.initialize(Calendar.dateFromString(args.fromDay),Calendar.dateFromString(args.toDay))

    tradingContext.run()


