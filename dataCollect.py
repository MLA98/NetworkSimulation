# λ arrival lamdba
# u service 

import subprocess
import numpy as np 

serviceRate = '1';
arrivalRate = ['0.1', '0.2', '0.4', '0.5', '0.6', '0.8', '0.9'];
maxBufferSize = ['-1', '1', '20', '30']
script = './run.sh'
option = 'negExp'

class dataPerMaxBufferSize:
  def __init__(self, maxBufferSize):
    self.maxBufferSize = maxBufferSize
    self.meanQueueLength = []
    self.dropCount = []
    self.utilizationRate = []
    self.theoraticalUtilizationRate = []
    self.theoraticalMeanQueueLength = []
    self.arrivalRate = ['0.1', '0.2', '0.4', '0.5', '0.6', '0.8', '0.9'];
    self.maxBufferArr = []
    self.serviceRate = []
    if maxBufferSize != '-1':
      self.arrivalRate.pop(0)

    self.simulation()
  def simulation(self):
    for r in self.arrivalRate:
        result = subprocess.run([script, r, serviceRate, self.maxBufferSize, option], stdout=subprocess.PIPE).stdout.decode('utf-8').split('\n')
        data = result[len(result) - 2].split(' ')[-1]
        self.utilizationRate.append(data)
        data = result[len(result) - 3].split(' ')[-1]
        self.meanQueueLength.append(data)
        data = result[len(result) - 4].split(' ')[-1]
        self.dropCount.append(data)
        p  = float(r) / float(serviceRate)
        self.theoraticalUtilizationRate.append(p)
        self.theoraticalMeanQueueLength.append((p) / (1 - p))
        self.maxBufferArr.append(self.maxBufferSize)
        self.serviceRate.append(1)

class globalData:
  def __init__(self, globalArrival, globalMaxBuffer, globalDrop, globalMeanQ, globalUtilizationR, globalService):
    self.globalArrival = globalArrival
    self.globalMaxBuffer = globalMaxBuffer
    self.globalDrop = globalDrop
    self.globalMeanQ = globalMeanQ
    self.globalUtilizationR = globalUtilizationR
    self.globalService = globalService

def generateData():
  dataAll = []
  dataInf = dataPerMaxBufferSize('-1')
  dataOne = dataPerMaxBufferSize('1')
  dataTwenty = dataPerMaxBufferSize('20')
  dataThirty = dataPerMaxBufferSize('30')
  dataAll.append(dataInf)
  dataAll.append(dataOne)
  dataAll.append(dataTwenty)
  dataAll.append(dataThirty)

  globalArrival = []
  globalMaxBuffer = []
  globalDrop = []
  globalMeanQ = []
  globalUtilizationR = []
  globalService = []

  for d in dataAll:
    globalArrival += d.arrivalRate
    globalMaxBuffer += d.maxBufferArr
    globalDrop += d.dropCount
    globalMeanQ += d.meanQueueLength
    globalUtilizationR += d.utilizationRate
    globalService += d.serviceRate


  globalArrival = np.array(globalArrival) 
  globalArrival = globalArrival.astype(np.float) 

  globalMaxBuffer = np.array(globalMaxBuffer) 
  globalMaxBuffer = globalMaxBuffer.astype(np.float) 

  globalDrop = np.array(globalDrop) 
  globalDrop = globalDrop.astype(np.float) 

  globalMeanQ = np.array(globalMeanQ) 
  globalMeanQ = globalMeanQ.astype(np.float) 

  globalUtilizationR = np.array(globalUtilizationR) 
  globalUtilizationR = globalUtilizationR.astype(np.float) 
  globalService = np.array(globalService)

  return globalData(globalArrival, globalMaxBuffer, globalDrop, globalMeanQ, globalUtilizationR, globalService)


# data = generateData()
# print(data.globalArrival)
# print(data.globalMaxBuffer)
# print(data.globalDrop)
# print(data.globalMeanQ)
# print(data.globalUtilizationR)
# print(data.globalService)






