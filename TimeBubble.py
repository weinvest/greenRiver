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
        if self.isEmpty():
            return None

        currentTime, task = self.tasks[0]
        self.timeLine.time = currentTime

        while not self.isEmpty():
            taskTime, task = self.tasks[0]
            if currentTime == taskTime:
                self.pop()
                if task.bubble():
                    self.add(task)
            else:
                break
        return currentTime

