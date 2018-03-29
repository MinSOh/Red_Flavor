import numeric_study_model as nsm
from Model import model
from MegaVariableInterpreter import interpreter
import math
import numpy as np

class Learner:
    def __init__(self,asset_list):
        self.asset_list = asset_list
        self.model = model(stateN=[], evidenceN=[], totalLength=0, evidence_dic={}, T_list=[], S_list=[], P_X0=[],
                 forward_message=[])
        self.interpreterList_state = []
        self.interpreterList_sensor = [None]
        self.maxStep = 0

    def reset(self):
        self.asset_list = []
        self.model = self.model.reset()
        self.interpreterList_state = []
        self.interpreterList_sensor = [None]
        self.maxStep = 0

    def initialize(self):
        stateN = []
        evidenceN = [None]
        S_list = [None]
        T_list = []
        temp = self.asset_list[0]
        stateN.append(math.pow(2,temp))
        self.interpreterList_state.append(interpreter((2,) * temp))
        for i in range(1, len(self.asset_list)):
            temp = int(self.asset_list[i])
            stateN.append(int(math.pow(2,temp)))
            evidenceN.append(int(math.pow(3,temp)))
            self.interpreterList_state.append(interpreter((2,)*temp))
            self.interpreterList_sensor.append(interpreter((3,)*temp))
        for i in range(len(self.asset_list)-1):
            m = self.asset_list[i+1]
            n = self.asset_list[i]
            T = nsm.making_asset_transition_model(m,n)
            S = nsm.making_asset_sensor_model(m)
            T_list.append(T)
            S_list.append(S)
        P_X0 = [1.0] * int(stateN[0])
        P_X0 = np.array(P_X0)
        P_X0 = np.reshape(P_X0, (-1, 1))
        P_X0 = P_X0 / float(stateN[0])

        self.model = model(stateN=stateN,evidenceN=evidenceN,T_list=T_list,S_list=S_list,P_X0=P_X0,
                 forward_message=[],backward_message_dic = {},predict_message_dic = {},applied_evidence = {},evidence_dic={})
        self.model.initialize()

    def get_model(self):
        return self.model

    def get_asset_list(self):
        return self.asset_list
    def get_interpreterList_state(self):
        return self.interpreterList_state
    def get_interpreterLIst_sensor(self):
        return self.interpreterList_sensor

    def activity(self,t,act_tuple):
        if len(act_tuple) == self.asset_list[t]:
            if(t > self.maxStep):
                self.maxStep = t
            interp = self.interpreterList_sensor[t]
            self.model.update_evidence(t,interp.tuple_to_int(act_tuple))
        else:
            print('[Error] [Learner -> activity] tuple\'s length must be equal to number of asset at step t (='+str(self.asset_list[t])+')')

    def analyze_all(self):
        if self.maxStep == 0:
            print('[Warn] [Learner -> activity] There are no activity!')
            return None
        result = []
        self.model.apply_current_evidences()
        for i in range(self.maxStep + 1):
            result.append(self.model.mle_mega(i,self.interpreterList_state[i]))
        return result

    def get_probability(self,t):
        temp = self.model.get_probability_mega(t,self.interpreterList_state[t])
        result = []
        for i in range(len(temp)):
            result.append(temp[i][1][0])
        return result

