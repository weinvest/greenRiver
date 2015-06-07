__author__ = 'shgli'
import heapq
import datetime

class TimeBuble(object):
    def __init__(self):
        self.tasks = []
        self.lastTime = datetime.datetime(1970,0,0)

    def add(self, task):
        heapq.heappush(self.tasks, (task.time, task))

    def pop(self):
        return heapq.heappop(self.tasks)

    def isEmpty(self):
        return 0 == len(self.tasks)

    def process(self, processId):
        if not self.isEmpty():
            curtime, task = self.pop()
            while not self.isEmpty() and curtime == self.tasks[0][0]:
                task.process(processId)

