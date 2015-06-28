__author__ = 'shgli'
from IFeederCreator import IFeederCreator
from LocalFeeder import LocalFeeder
class LocalFeederCreator(IFeederCreator):
    def __init__(self,path):
        self.path = path

    def create(self,instrument):
        return LocalFeeder(instrument, self.path)

    def adjustStartDay(self, day):
        pass

    def adjustEndDay(self, day):
        pass