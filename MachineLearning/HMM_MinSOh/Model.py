import RandomData as rd
import helper
import numpy as np


#     apply_current_evidences -> smoothing
#  == get_probability

class model:
    def __init__(self, stateN=[], evidenceN=[], totalLength=0, evidence_dic={}, T_list=[], S_list=[], P_X0=[],
                 forward_message=[],backward_message_dic = {},predict_message_dic = {},applied_evidence = {}):
        '''

        :param stateN: list
        :param evidenceN: list
        :param totalLength: int
        :param evidence_dic: dictionary
        :param T_list: list
        :param S_list: list
        :param P_X0: list
        '''
        self.stateN = stateN
        self.evidenceN = evidenceN
        self.totalLength = totalLength
        self.evidence_dic = evidence_dic
        self.T_list = T_list
        self.S_list = S_list
        self.P_X0 = P_X0
        self.forward_message = forward_message
        self.backward_message_dic = {} #It is JUST temporary storage
        self.predict_message_dic = {}
        self.applied_evidence = {}

    def reset(self):
        self.stateN = []
        self.evidenceN = []
        self.totalLength = 0
        self.evidence_dic = {}
        self.T_list =[]
        self.S_list = []
        self.P_X0 = []
        self.forward_message = []
        self.backward_message_dic = {}
        self.predict_message_dic = {}
        self.applied_evidence = {}

    def initialize(self, option=0):
        '''
        :param option: 0 -> with no change (just checking robustness)
                option: 1 -> with random P_X0, evidence_dic ,Transition model and Sensor model (robust itself)
        '''
        print('[Info] Initialize...')
        if (option == 0):
            length = len(self.stateN)
            if length == len(self.evidenceN):
                if length - 1 == len(self.T_list):
                    for i in range(length - 1):
                        if self.T_list[i].shape == (self.stateN[i + 1], self.stateN[i]):
                            continue
                        else:
                            print('[Error] [initialize] Wrong Transition Model at t = ' + str(i) + '(wrong matrix P(X_t+1|X_t)')
                            return False
                    if length == len(self.S_list):
                        if self.S_list[0] != None:
                            print('[Error] [initialize] First state X_0 has no evidence model')
                            return False
                        for i in range(length - 1):
                            if self.S_list[i + 1].shape == (self.stateN[i + 1], self.evidenceN[i + 1]):
                                continue
                            else:
                                print('[Error] [initialize] Wrong Sensor Model at t = ' + str(i) + '(wrong matrix P(e_t|x_t)')
                                return False
                        if helper.checking_validity_S_list(self.S_list) and helper.checking_validity_T_list(
                                self.T_list):
                            if helper.checking_validity_T_list(self.T_list):
                                if self.stateN[0] == len(self.P_X0):
                                    if helper.checking_validity_P_X0(self.P_X0):
                                        self.totalLength = length
                                        self.forward_message.append(self.P_X0)
                                        self.predict_message_dic.update({0:self.P_X0})
                                        ###################################Printing###########################################
                                        if self.totalLength == 0:
                                            print('[Error] [initialize] There are no node!')
                                            return False
                                        elif self.totalLength == 1:
                                            print('[Warn] [initialize] Meaningless Model : X0')
                                            return True
                                        elif self.totalLength == 2:
                                            print('[Info] Success!')
                                            print('[Info] [initialize] ValidModel: X0 -> X1')
                                            print('                                      |')
                                            print('                                      e1')
                                            return True
                                        elif self.totalLength == 3:
                                            print('[Info] Success!')
                                            print('[Info] [initialize] ValidModel: X0 -> X1 -> X2')
                                            print('                                      |     |')
                                            print('                                      e1    e2')
                                            return True
                                        else:
                                            print('[Info] Success!')
                                            print('[Info] [initialize] Valid Model :X0 -> X1 -> ... -> X' + str(self.totalLength - 1))
                                            print('                                       |            |')
                                            print('                                       e1           e' + str(self.totalLength - 1))
                                            return True
                                        ######################################################################################
                                    else:
                                        print('[Error] [initialize] Probability invalid: P(X_0) (Sum of Probability must be 1)')
                                        return False
                                else:
                                    print('[Error] [initialize] Probability invalid: P(X_0) (stateN[0] == len(P_X0)')
                                    return False
                            else:
                                print('[Error] [initialize] Probability invalid: T_list')
                                return False
                        else:
                            print('[Error] [initialize] Probability invalid: S_list')
                            return False
                    else:
                        print('[Error] [initialize] Model should have same length of stateN and S_list')
                        return False
                else:
                    print('[Error] [initialize] Model should have same length of stateN and T_list')
                    return False
            else:
                print('[Error] [initialize] Model should have same length of stateN and evidenceN')
                return False
        elif (option == 1):
            if len(self.stateN) == len(self.evidenceN):
                self.totalLength = len(self.stateN)
                self.P_X0 = rd.Making_Random_FirstState_Probability(self.stateN)
                self.evidence_dic = rd.Making_Random_Evidence_Dic(self.evidenceN)
                self.T_list = rd.Making_Random_Transition_Model(self.stateN)
                self.S_list = rd.Making_Random_Sensor_Model(self.stateN, self.evidenceN)
                self.forward_message.append(self.P_X0)
                self.predict_message_dic.update({0:self.P_X0})

                ###################################Printing###########################################
                if self.totalLength == 0:
                    print('[Error][initialize] There are no node!')
                    return False
                elif self.totalLength == 1:
                    print('[Warn] [initialize] Meaningless Model : X0')
                elif self.totalLength == 2:
                    print('[Info] Success!')
                    print('[Info] [initialize] ValidModel: X0 -> X1')
                    print('                                      |')
                    print('                                      e1')
                elif self.totalLength == 3:
                    print('[Info] Success!')
                    print('[Info] [initialize] ValidModel: X0 -> X1 -> X2')
                    print('                                      |     |')
                    print('                                      e1    e2')
                else:
                    print('[Info] Success!')
                    print('[Info] [initialize] Valid Model :X0 -> X1 -> ... -> X' + str(self.totalLength - 1))
                    print('                                       |            |')
                    print('                                       e1           e' + str(self.totalLength - 1))
                    print('[Info] Success!')
                ######################################################################################
            else:
                print('[Error] [initialize] Model should have same length of stateN and evidenceN')
                return False
            return True
        else:
            print('[Error] [initialize] Option is 0 or 1')
            print('                     option=0 : with random Transition and Sensor model')
            print('                     option=1 : with no change of T_list and S_list')
            return False

    def add_initial(self, number_of_state):
        if self.totalLength > 0:
            print('[Error] [add_initial] Model cannot have more than one initial node')
            return None
        self.stateN.append(number_of_state)
        self.evidenceN.append(None)
        self.totalLength = self.totalLength + 1

    def add(self, number_of_state, number_of_evidence):
        if self.totalLength == 0:
            print('[Error] [add] Model must have initial state X_0')
            return None
        self.stateN.append(number_of_state)
        self.evidenceN.append(number_of_evidence)
        self.totalLength = self.totalLength + 1

    def add_as_list(self, list_of_state, list_of_evidence):
        if self.totalLength == 0 and list_of_evidence[0] != None:
            print('[Error] [add_as_list] Initial Node must have no evidence')
            return None
        if len(list_of_state) == len(list_of_evidence):
            self.stateN = self.stateN + list_of_state
            self.evidenceN = self.evidenceN + list_of_evidence
            self.totalLength = self.totalLength + len(list_of_evidence)
        else:
            print('[Error] [add_as_list] length of two input list should be equal')
            return None

    def get_stateN(self):
        return self.stateN

    def get_evidenceN(self):
        return self.evidenceN

    def get_totalLength(self):
        return self.totalLength

    def get_S_list(self):
        return self.S_list

    def get_T_list(self):
        return self.T_list

    def get_evidence_dic(self):
        return self.evidence_dic

    def get_forward_message(self):
        return self.forward_message

    def get_predict_message_dic(self):
        return self.predict_message_dic

    def get_backward_message_dic(self):
        return self.backward_message_dic

    def get_P_X0(self):
        return self.P_X0

    def ingest_evidence_dic(self,dictionary):
        for i in dictionary.keys():
            self.ingest_evidence(i,dictionary[i])
        return dictionary

    def ingest_evidence(self, t, evidence):
        if t in self.evidence_dic.keys():
            print('[Warn] [ingest_evidence] There exist evidence at step '+str(t)+' , already. If you want update, use update_evidence.')
            print('                         **update_evidence will recalculate forward message')
            return None
        self.evidence_dic.update({t: evidence})
        return {t: evidence}

    def update_evidence(self,t,evidence):
        m = max(max(self.predict_message_dic.keys()),len(self.forward_message)-1)
        self.forward_message = self.forward_message[:t]
        self.evidence_dic.update({t:evidence})
        self.update_forward_message(m)
        return {t: evidence}


    def update_evidence_dic(self,dictionary):
        mini = min(dictionary.keys)
        m = max(max(self.predict_message_dic.keys()), len(self.forward_message))
        self.forward_message = self.forward_message[:mini]
        for i in dictionary.keys():
            self.evidence_dic.update({i:dictionary[i]})
        self.update_forward_message(m)
        return dictionary

    def del_evidence(self, t):
        temp = self.evidence_dic[t]
        del self.evidence_dic[t]
        return temp

    def del_evidence_all(self):
        self.evidence_dic = {}
        return self.evidence_dic

    def set_S_list(self, S_list):
        self.S_list = np.array(S_list)
        return self.S_list

    def set_T_list(self, T_list):
        self.T_list = np.array(T_list)
        return self.T_list

    def set_P_X0(self, P_X0):
        P_X0 = np.array(P_X0)
        P_X0 = np.reshape(P_X0, (-1, 1))
        self.P_X0 = P_X0
        return self.P_X0

    def print_needed_data_format(self):
        S_list = [None]
        T_list = []
        P_X0 = (self.stateN[0], 1)
        for i in range(len(self.stateN)-1):
            S_list.append((self.stateN[i+1],self.evidenceN[i+1]))
            T_list.append((self.stateN[i+1],self.stateN[i]))
        print('#######Data Format#######')
        print('S_list: ',end='')
        print(S_list)
        print('T_list: ',end='')
        print(T_list)
        print('P_X0: ',end='')
        print(P_X0)
        print('#########################')
    ####### Algorithms ######

    def calculate_onestep(self, t):
        if len(self.forward_message) > t:
            return 0
        elif len(self.forward_message) == t and (t in self.evidence_dic.keys()):
            S = self.S_list[t][:, self.evidence_dic[t]]
            S = np.reshape(S, (-1, 1))
            self.forward_message.append(
                helper.normalize(np.multiply(S, np.dot(self.T_list[t - 1], self.forward_message[t - 1]))))
            return 1
        elif len(self.forward_message) == t:
            self.predict_message_dic.update({t: np.dot(self.T_list[t - 1], self.forward_message[t - 1])})
            return 2
        elif t-1 in self.predict_message_dic.keys():
            self.predict_message_dic.update({t: np.dot(self.T_list[t - 1], self.predict_message_dic[t - 1])})
            return 2
        else:
            print('[Error] [calculate_onestep] You should know before step ' + str(t - 1) + ' \'s message')
            return -1

    def update_forward_message(self, t):
        '''
        :param t: It calculate forward_message or predict_message until step t
        :return: If there exist f_message at t already, then return 0
                else if we can calculate f_message at t, then return 1
                else we calculate predict_message at t and return 2
                return -1 if error
        '''
        if len(self.forward_message) > t:
            return 0, 0
        else:
            cur_len = len(self.forward_message)
            cur_st = 0
            st = 0
            for i in range(cur_len, t + 1):
                temp = self.calculate_onestep(i)
                if temp > cur_st:
                    cur_st = temp
                    st = i
            return cur_st, st

    def update_forward_message_with_log(self, t):
        log, st = self.update_forward_message(t)
        if log == 0:
            print('[Info] All forward messages are Already Calculated')
        elif log == 1:
            print('[Info] Some forward messages are newly Calculated from step ' + str(st) + '.')
        elif log == 2:
            print('[Info] Predict messages are calculated (from step ' + str(len(self.forward_message)) + '.)')

    def recalculate_forward_message(self):
        m = max(self.evidence_dic.keys())
        self.forward_message = self.forward_message[:1]
        self.update_forward_message(m)

    def clear_backward(self):
        self.backward_message_dic = {}
        return self.backward_message_dic

    def jump_transition(self,i,j):
        '''

        :param i:
        :param j:
        :return: P(X_j|X_i)
        '''
        result = self.T_list[i]
        for p in range(j-i-1):
            result = np.dot(self.T_list[i+1+p],result)

        return result

    def backward_all(self):
        current_state_fix = max(self.evidence_dic.keys())
        current_state = current_state_fix
        temp = self.stateN[current_state]
        one = [1]*temp
        one = np.array(one)
        one = np.reshape(one,(temp,1))
        self.backward_message_dic.update({current_state_fix:one})
        for i in range(current_state_fix):
            j = current_state_fix-1-i
            T = self.jump_transition(j,current_state)
            m,n = T.shape
            S = self.S_list[current_state][:,self.evidence_dic[current_state]]
            S = np.reshape(S,(-1,1))
            S_span = helper.span(S,n)
            b_current_state = self.backward_message_dic[current_state]
            b_cur_span = helper.span(b_current_state,n)
            temp = np.multiply(S_span,b_cur_span)
            temp = np.multiply(temp,T)
            temp = temp.sum(axis=0)
            temp = np.reshape(temp,(n,1))
            self.backward_message_dic.update({j:temp})
            if j in self.evidence_dic.keys():
                current_state = j
        self.applied_evidence = self.evidence_dic

    def smoothing(self,t):
        if len(self.forward_message) > t:
            if t in self.backward_message_dic.keys():
                if self.evidence_dic == self.applied_evidence:
                    return helper.normalize(np.multiply(self.forward_message[t],self.backward_message_dic[t]))
                else:
                    print('[Error] [smoothing] There are some new evidence. Please do backward_all, again.')
                    return None
            else:
                print('[Error] [smoothing] It need backward message. Please do backward_all.')
                return None
        else:
            if t in self.predict_message_dic.keys():
                if t in self.backward_message_dic.keys():
                    if self.evidence_dic == self.applied_evidence:
                        return helper.normalize(np.multiply(self.predict_message_dic[t], self.backward_message_dic[t]))
                    else:
                        print('[Error] [smoothing] There are some new evidence. Please do backward_all, again.')
                        return None
                else:
                    print('[Error] [smoothing] It need backward message. Please do backward_all.')
                    return None
            else:
                print('[Error] [smoothing] Update Forward Message or Do apply_current_evidences, first.')
                return None

    def apply_current_evidences(self):
        current_state = max(self.evidence_dic.keys())
        self.update_forward_message(current_state)
        self.clear_backward()
        self.backward_all()

    def get_probability(self,t):
        self.apply_current_evidences()
        if t in self.backward_message_dic.keys():
            if t < len(self.forward_message):
                return helper.normalize(np.multiply(self.forward_message[t],self.backward_message_dic[t]))
            else:
                return helper.normalize(np.multiply(self.predict_message_dic[t],self.backward_message_dic[t]))
        else:
            self.update_forward_message(t)
            return self.predict_message_dic[t]

    def mle(self,t):
        v = self.get_probability(t)
        return helper.maxProb_fromVector(v)


    def get_probability_mega(self,t,intptr):
        shape = intptr.get_shape()
        reshaped = np.reshape(self.get_probability(t),shape)
        result = []
        for i in range(len(shape)):
            result.append(helper.sum_remain_oneDimension(reshaped,i))
        return result

    def mle_mega(self,t,intptr):
        l = self.get_probability_mega(t,intptr)
        result = []
        for i in range(len(l)):
            result.append(helper.maxProb_fromVector(l[i]))
        return tuple(result)

    def remove_all_forward_message(self):
        self.forward_message = self.forward_message[:1]
        return self.forward_message

    def current_max_evidence_index(self):
        return max(self.evidence_dic.keys())











