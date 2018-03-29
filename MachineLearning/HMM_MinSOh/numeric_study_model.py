import math
import numpy as np
from MegaVariableInterpreter import interpreter

sensor_element = np.array([[0.4,0.4,0.2],
                           [0.25,0.05,0.7]])

def knowingProb(mega_tuple):
    n0 = 0
    n1 = 0
    for i in range(len(mega_tuple)):
        if mega_tuple[i] == 0:
            n0 = n0 + 1
        else:
            n1 = n1 + 1
    n0 = float(n0)
    n1 = float(n1)
    half_weight = math.sqrt(n0 * n1 + 1.0) / math.pow(n0 + n1, 2)
    avg = n1/(n0+n1)
    weighted_avg = (half_weight*0.5 + avg)/(1+half_weight)
    return weighted_avg

def apply_multiply(mega_tuple,p):
    result = 1
    for i in range(len(mega_tuple)):
        if mega_tuple[i] == 1:
            result = result*p
        else:
            result = result*(1-p)
    return result

def making_asset_transition_model(m_assets,n_assets):
    m = int(math.pow(2,m_assets))
    n = int(math.pow(2,n_assets))
    m_tuple = (2,)*m_assets
    n_tuple = (2,)*n_assets
    intr_m = interpreter(m_tuple)
    intr_n = interpreter(n_tuple)
    result = np.zeros((m,n))
    for j in range(n):
        pj = knowingProb(intr_n.int_to_tuple(j))
        for i in range(m):
            mt = intr_m.int_to_tuple(i)
            result[i][j] = apply_multiply(mt,pj)
    return result

def making_asset_sensor_model(n_assets):
    n = int(math.pow(2,n_assets))
    s = int(math.pow(3,n_assets))
    result = np.zeros((n,s))
    n_tuple = (2,)*n_assets
    s_tuple = (3,)*n_assets
    intr_n = interpreter(n_tuple)
    intr_s = interpreter(s_tuple)
    for i in range(n):
        nt = intr_n.int_to_tuple(i)
        for j in range(s):
            st = intr_s.int_to_tuple(j)
            temp = 1
            for k in range(len(st)):
                temp = temp * sensor_element[nt[k]][st[k]]
            result[i][j] = temp
    return result

