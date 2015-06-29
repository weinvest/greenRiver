__author__ = 'shgli'
import heapq
import datetime

class TimeBuble(object):
    def __init__(self,timeLine):
        self.tasks = []
        self.timeLine = timeLine

    def add(self, task):
        nextTime = task.getNextTime()
        if nextTime:
            heapq.heappush(self.tasks, (nextTime, task))

    def pop(self):
        return heapq.heappop(self.tasks)

    def isEmpty(self):
        return 0 == len(self.tasks)

    def bubble(self):
        if not self.isEmpty():
            curtime, task = self.pop()
            self.timeLine = curtime
            while not self.isEmpty() and curtime == task.getNextTime():
                if task.bubble():
                    self.add(task)
                task = self.pop()[1]

            return curtime

        return None

