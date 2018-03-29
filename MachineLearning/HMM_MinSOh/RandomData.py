import helper
import random
import numpy as np

def Making_Random_Sensor_Model(stateN,evidenceN):
    result = [None]
    for i in range(len(stateN)-1):
        x = np.random.randint(1,50,size=(stateN[i+1],evidenceN[i+1]))
        temp = []
        for j in range(len(x)):
            temp.append(helper.normalize(x[j]))
        temp = np.array(temp)
        temp = np.reshape(temp,(stateN[i+1],evidenceN[i+1]))
        result.append(temp)
    return result

def Making_Random_Transition_Model(stateN):
    result = []
    for i in range(len(stateN)-1):
        m = stateN[i+1]
        n = stateN[i]
        x = np.random.randint(1, 50, size=(n,m))
        temp = []
        for j in range(len(x)):
            temp.append(helper.normalize(x[j]))
        temp = np.array(temp)
        temp = temp.transpose()
        temp = np.reshape(temp, (m, n))
        result.append(temp)
    return result

def Making_Random_FirstState_Probability(stateN):
    x = np.random.randint(1,50,size=(stateN[0],1))
    x = helper.normalize(x)
    return x

def Making_Random_Evidence_Dic(evidenceN):#X0에서는 evidence안받음
    result = [None]
    dic = {}
    for i in range(len(evidenceN)-1):
        x = random.randrange(0,evidenceN[i+1])
        result.append(x)
    for i in range(len(result)):
        dic.update({i:result[i]})
    return dic