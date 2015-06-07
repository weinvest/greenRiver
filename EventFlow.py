__author__ = 'shgli'
from toposort import toposort_flatten


class EventFlow(object):
    def __init__(self):
        self.changed = False
        self.nodes = set()
        self.raisedNodes = []
        self.maxLevel = []

    def setChanged(self):
        self.changed = True

    def addNode(self, node):
        self.nodes.add(node)
        self.setChanged()

    def add2RunList(self,level, node):
        while len(self.raisedNodes) <= level:
            self.raisedNodes.append(set())
        self.raisedNodes[level].add(node)

    def assignLevel(self):
        dependencyDict = {}
        for node in self.nodes:
            dependencyDict[node] = node.precursors
        self.maxLevel = 0
        nodes = toposort_flatten(dependencyDict)
        for node in nodes:
            maxLevel = -1
            for precursor in node.precursors:
                maxLevel = max(maxLevel, node.level)
            node.level = maxLevel + 1
            self.maxLevel = max(self.maxLevel,node.level)

    def process(self,processId):
        runList = self.raisedNodes
        self.raisedNodes = []

        for level in range(0,self.maxLevel + 1):
            for node in runList[level]:
                node.process(processId)

        self.assignLevel()


