import numpy as np
from numpy import array as arr
import math


def normalize(l):
    total = 0
    for i in l:
        total += i
        total = float(total)
    if total == 0:
        return arr([1]*len(l))/len(l)
    return arr(l)/total

#to_oneD_list : column vector to list
def to_oneD_list(l):
    l = np.reshape(l,(1,-1))
    return l[0]

def maxProb_fromVector(l):
    l = to_oneD_list(l)
    maxidx = 0
    max = l[0]
    for i in range(len(l)-1):
        if max < l[i+1]:
            maxidx = i+1
            max = l[i+1]
    return maxidx

def maxProb_fromList(l):
    maxidx = 0
    max = l[0]
    for i in range(len(l) - 1):
        if max < l[i + 1]:
            maxidx = i + 1
            max = l[i + 1]
    return maxidx

def column_normalize(matrix):
    temp = matrix.transpose()
    result = []
    for i in range(len(temp)):
        result.append(normalize(temp[i]))
    result = np.array(result)
    return result.transpose()

def interpreter_toInteger(n,list):
    result = int(0)
    for i in range(len(list)):
        result = int(result + list[i]*math.pow(n,i))
    return result

def interpreter_toList(n,integer):
    remainder = integer
    result = []
    while(remainder != 0):
        temp = remainder % n
        result.append(int(temp))
        remainder = (remainder - temp)/n
    return result

def checking_validity_S_list(S_list, epsilon=0.000001):
    if S_list[0] != None:
        print('S_list[0] must be None')
        return None
    for i in range(len(S_list)-1):
        temp = S_list[i+1].sum(axis=1)
        for j in range(len(temp)):
            if abs(temp[j] - 1) > epsilon:
                print('error : Where t = ' + str(i+1) +' and X_t = ' + str(j) +' , Sigma P(e_t|X_t) is not 1.')
                return False
    return True

def checking_validity_T_list(T_list,epsilon=0.000001):
    for i in range(len(T_list)):
        temp = T_list[i].sum(axis=0)
        for j in range(len(temp)):
            if abs(temp[j] - 1) > epsilon:
                print('error : Where t = ' + str(i) +' and X_t = ' + str(j) +' , Sigma P(X_t+1|X_t) is not 1.')
                return False
    return True

def checking_validity_P_X0(P_X0,epsilon=0.000001):
    if P_X0.sum(axis=0)-1 > epsilon:
        print('error : initial probability')
        return False
    return True

def span(vector,n):
    result = vector
    for i in range(n-1):
        result = np.concatenate((result,vector),axis=1)
    return result

def sup(list,upperbound):
    '''

    :param list: positive number list for searching
    :param upperbound: ''
    :return:  In list, find the supremum that below upperbound
    '''
    max = 0
    for i in range(len(list)):
        temp = list[i]
        if max < temp and temp <upperbound:
            max = temp
    return max

def sum_remain_oneDimension(matrix, n):
    result = matrix
    if n < len(matrix.shape):
        for i in range(len(matrix.shape)):
            if i != n:
                result = result.sum(axis=i,keepdims=True)
        return np.reshape(result,(-1,1))
    else:
        print('[Error] [sum_remain_oneDimension] input integer n must be smaller than Dim(matrix)')
        return None


