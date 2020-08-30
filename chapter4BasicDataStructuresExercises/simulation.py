from pythonds.basic import Queue

import random

class Team:
    def __init__(self, worker1 = None, worker2 = None, worker3 = None):
        self.worker1 = worker1
        self.worker2 = worker2
        self.worker3 = worker3
        self.workers = [worker1, worker2, worker3]
        self.numberOfWorkers = 0
        for worker in self.workers:
            if worker != None:
                self.numberOfWorkers +=1
            else:
                self.workers.pop(self.workers.index(worker))
       
    def allBusy(self):
        return len(self.whoIsFree()) == 0

    def whoIsFree(self):
       return [worker for worker in self.workers if worker.busy == False]

    def assignTask(self,task):
        if allBusy():
            self.workers[random.randrange(0,numberOfWorkers)].addTask(task)
        else:
            self.whoIsFree()[0].addTask(task)

    def tick(self):
        for worker in self.workers:
            worker.tick()


class Worker:
    def __init__(self, workrate):
        self.work= workrate
        self.currentTask = None
        self.timeRemaining = 0
        self.taskList = Queue()

    def tick(self):
        if self.currentTask != None:
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining <= 0:
                self.currentTask = None
                if self.taskList.isEmpty() == False:           
                    self.startNext()

    def busy(self):
        if self.currentTask != None:
            return True
        else:
            return False

    def addTask(self,task):
        self.taskList.push(task)

    def startNext(self):
        self.currentTask = self.taskList.pop()
        self.timeRemaining = newtask.getDifficulty() * 60/self.work

class Task:
    def __init__(self,time):
        self.timestamp = time
        self.difficulty = random.randrange(1,21)

    def getStamp(self):
        return self.timestamp

    def getDifficulty(self):
        return self.difficulty

    def waitTime(self, currenttime):
        return currenttime - self.timestamp


def simulation(numSeconds, tasksPerMinute):

    worker1 = Worker(2)
    worker2 = Worker(3)
    worker3 = Worker(4)

    team = Team(worker1, worker2, worker3)

    taskQueue = Queue()
    waitingtimes = []

    for currentSecond in range(numSeconds):

      if newTask():
         task = Task(currentSecond)
         taskQueue.enqueue(task)

      if (not team.allBusy()) and (not taskQueue.isEmpty()):
        nextTask = taskQueue.dequeue()
        team.assignTask(nextText())
        waitingtimes.append( nexttask.waitTime(currentSecond))
        team.assignTask()

      team.tick()

    averageWait=sum(waitingtimes)#/len(waitingtimes)
    print("Average Wait %6.2f secs %3d tasks remaining."%(averageWait,taskQueue.size()))

def newTask():
    num = random.randrange(1,181)
    if num == 180:
        return True
    else:
        return False

for i in range(10):
    simulation(3600,5)
