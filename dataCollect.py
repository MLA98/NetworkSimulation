# λ arrival lamdba
# u service 

import subprocess

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
    self.theoraticalUtilizationRate = [];
    self.theoraticalMeanQueueLength = [];
    self.simulation()
  def simulation(self):
    for r in arrivalRate:
        result = subprocess.run([script, r, serviceRate, self.maxBufferSize, option], stdout=subprocess.PIPE).stdout.decode('utf-8').split('\n')
        print(result)
        data = result[len(result) - 2].split(' ')[-1]
        self.utilizationRate.append(data)
        data = result[len(result) - 3].split(' ')[-1]
        self.meanQueueLength.append(data)
        data = result[len(result) - 4].split(' ')[-1]
        self.dropCount.append(data)
        p  = float(r) / float(serviceRate)
        self.theoraticalUtilizationRate.append(p)
        self.theoraticalMeanQueueLength.append((p) / (1 - p))




dataInf = dataPerMaxBufferSize('-1')
dataOne = dataPerMaxBufferSize('1')
dataTwenty = dataPerMaxBufferSize('20')
dataThirty = dataPerMaxBufferSize('30')


print(dataTwenty.meanQueueLength)
print(dataTwenty.theoraticalMeanQueueLength)
print(dataTwenty.utilizationRate)
print(dataTwenty.theoraticalUtilizationRate)
