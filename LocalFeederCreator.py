__author__ = 'shgli'
from IFeederCreator import IFeederCreator
from LocalFeeder import LocalFeeder
class LocalFeederCreator(IFeederCreator):
    def __init__(self,path):
        self.path = path

    def create(self,instrument,timeLine):
        return LocalFeeder(instrument, timeLine, self.path)

    def adjustStartDay(self, day):
        return day

    def adjustEndDay(self, day):
        return day