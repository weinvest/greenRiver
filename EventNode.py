__author__ = 'shgli'


class EventNode(object):
    def __init__(self, name):
        self.name = name;
        self.successors = set()
        self.precursors = set()
        self.eventFlow = None
        self.level = 0
        self.beRaised = False

    def setEventFlow(self, eventFlow):
        self.eventFlow = eventFlow
        eventFlow.addNode(self)

    def connect(self, other):
        other.precursors.add(self)
        self.successor.add(other)
        self.eventFlow.setChanged()

    def disconnect(self, other):
        other.precursors.remove(self)
        self.successor.remove(other)
        self.eventFlow.setChanged()

    def raiseSelf(self):
        if not self.beRaised:
            self.beRaised = True
            self.eventFlow.add2RunList(self.level, self)

    def raiseSuccessor(self):
        for successor in self.successors:
            successor.raiseSelf()

    def process(self, processId):
        self.beRaised = False
        self.doProcess(processId)

    def doProcess(self, processId):
        pass

