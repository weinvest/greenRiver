__author__ = 'shgli'

import os
import datetime
from exceptions import Exception
class Calendar(object):

    def __init__(self,holidayFile):
        self.holidays = []
        for holidayLine in holidayFile:
            holidayLine = holidayLine.strip()
            if 8 == len(holidayLine) and holidayLine[0] != '#':
                print(holidayLine)
                holiday = self.dateFromString(holidayLine)
                self.holidays.append(holiday)

    def getPreviousTradingDay(self,day):
        previousTradingDay = day + datetime.timedelta(days=-1)
        while not self.isTradingDay(previousTradingDay):
            previousTradingDay = previousTradingDay + datetime.timedelta(days=-1)

        return previousTradingDay

    def getNextTradingDay(self,day):
        nextTradingDay = day + datetime.timedelta(days=1)
        while not self.isTradingDay(nextTradingDay):
            nextTradingDay = nextTradingDay + datetime.timedelta(days=1)

        return nextTradingDay

    def isHoliday(self,day):
        return day in self.holidays

    @classmethod
    def isBussinessDay(self,day):
        return day.weekday() <= 4

    def isTradingDay(self,day):
        return self.isBussinessDay(day) and not self.isHoliday(day)

    @classmethod
    def dateFromString(self,strDay):
        '''eg. 20150612'''
        year = int(strDay[0:4])
        month = int(strDay[4:6])
        day = int(strDay[6:])
        return datetime.date(year,month,day)

    @classmethod
    def dateFromInt(cls,intDay):
        '''eg. int(20150612)'''
        year = intDay / 10000
        month = intDay % 10000 / 100
        day = intDay % 100
        return datetime.date(year,month,day)

    @classmethod
    def dateToString(cls,day):
        return day.strftime('%Y%m%d')

    @classmethod
    def dateToInt(cls,day):
        return day.year * 10000 + day.month * 100 + day.day

if __name__ == '__main__':
    import nose

    def test_dateFromInt():
        intDay = 20150624
        day = Calendar.dateFromInt(intDay)
        assert day.year == 2015
        assert day.month == 6
        assert day.day == 24

    def test_dateFromString():
        strDay = '20150624'
        day = Calendar.dateFromString(strDay)
        assert day.year == 2015
        assert day.month == 6
        assert day.day == 24

    def test_dateToString():
        day = Calendar.dateFromString('20150624')
        assert Calendar.dateToString(day) == '20150624'

    def test_dateToInt():
        day = Calendar.dateFromString('20150624')
        assert Calendar.dateToInt(day) == 20150624

    def test_isBussiness():
        assert Calendar.isBussinessDay(Calendar.dateFromString('20150601')) #monday
        assert Calendar.isBussinessDay(Calendar.dateFromString('20150602')) #tuesday
        assert Calendar.isBussinessDay(Calendar.dateFromString('20150603')) #wednesday
        assert Calendar.isBussinessDay(Calendar.dateFromString('20150604')) #thursday
        assert Calendar.isBussinessDay(Calendar.dateFromString('20150605')) #friday
        assert not Calendar.isBussinessDay(Calendar.dateFromString('20150606')) #saturday
        assert not Calendar.isBussinessDay(Calendar.dateFromString('20150607')) #sunday

    def setUp():
        holidays = ['#20150604','20150604','20150602']
        global ca
        ca = Calendar(holidays)

    def tearDown():
        global ca
        ca = None

    def test_isHoliday():
        assert ca.isHoliday(ca.dateFromString('20150604'))
        assert ca.isHoliday(ca.dateFromString('20150602'))
        assert not ca.isHoliday(ca.dateFromString('20150603'))

    def test_isTradingDay():
        assert ca.isTradingDay(ca.dateFromString('20150601'))
        assert not ca.isTradingDay(ca.dateFromString('20150602'))
        assert ca.isTradingDay(ca.dateFromString('20150603'))
        assert not ca.isTradingDay(ca.dateFromString('20150604'))
        assert ca.isTradingDay(ca.dateFromString('20150605'))
        assert not ca.isTradingDay(ca.dateFromString('20150606'))
        assert not ca.isTradingDay(ca.dateFromString('20150607'))

    def test_getPreviosTradingDay():
        assert ca.getPreviousTradingDay(ca.dateFromString('20150601')) == ca.dateFromString('20150529')
        assert ca.getPreviousTradingDay(ca.dateFromString('20150602')) == ca.dateFromString('20150601')
        assert ca.getPreviousTradingDay(ca.dateFromString('20150603')) == ca.dateFromString('20150601')
        assert ca.getPreviousTradingDay(ca.dateFromString('20150604')) == ca.dateFromString('20150603')
        assert ca.getPreviousTradingDay(ca.dateFromString('20150605')) == ca.dateFromString('20150603')
        assert ca.getPreviousTradingDay(ca.dateFromString('20150606')) == ca.dateFromString('20150605')
        assert ca.getPreviousTradingDay(ca.dateFromString('20150607')) == ca.dateFromString('20150605')

    def test_getNextTradingDay():
        assert ca.getNextTradingDay(ca.dateFromString('20150601')) == ca.dateFromString('20150603')
        assert ca.getNextTradingDay(ca.dateFromString('20150602')) == ca.dateFromString('20150603')
        assert ca.getNextTradingDay(ca.dateFromString('20150603')) == ca.dateFromString('20150605')
        assert ca.getNextTradingDay(ca.dateFromString('20150604')) == ca.dateFromString('20150605')
        assert ca.getNextTradingDay(ca.dateFromString('20150605')) == ca.dateFromString('20150608')
        assert ca.getNextTradingDay(ca.dateFromString('20150606')) == ca.dateFromString('20150608')
        assert ca.getNextTradingDay(ca.dateFromString('20150607')) == ca.dateFromString('20150608')

    nose.runmodule()