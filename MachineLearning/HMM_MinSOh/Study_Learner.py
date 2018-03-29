from Learner import Learn
import oll_helper
from MegaVariableInterpreter import interpreter

class oll_data_learner:
    def __init__(self,asset_list):
        self.asset_list = asset_list
        self.data_learn_list = []
        self.stateN = []

    def initialize(self):
        self.stateN = oll_helper.asset_list_to_stateN(self.asset_list)
        for i in range(len(self.asset_list)-1):
            temp = Learn(i,self.stateN[i+1],self.stateN[i])
            temp.initialize()
            self.data_learn_list.append(temp)

    def get_asset_list(self):
        return self.asset_list
    def get_step_t_Learner(self,t):
        return self.data_learn_list[t]
    def get_stateN(self):
        return self.stateN

    def get_step_t_history(self,t):
        return self.data_learn_list[t].get_history

    def ingest_tuples(self,step_t,step_t_tuple,step_tplus1_tuple,delta=1):
        interp_m = interpreter((2,)*self.asset_list[step_t+1])
        interp_n = interpreter((2,)*self.asset_list[step_t])
        self.data_learn_list[step_t].ingest(interp_m.tuple_to_int(step_tplus1_tuple),interp_n.tuple_to_int(step_t_tuple),delta)

    def make_T_list(self):
        T_list = []
        for i in range(len(self.data_learn_list)):
            T_list.append(self.data_learn_list[i].make_transition_model())
        return T_list

'''
a = oll_data_learner([2,3,4])
a.initialize()
for i in range(100):
    a.ingest_tuples(0,(random.randrange(0,2),random.randrange(0,2)),(random.randrange(0,2),random.randrange(0,2),random.randrange(0,2)))
for i in range(100):
    a.ingest_tuples(1,(random.randrange(0,2),random.randrange(0,2),random.randrange(0,2)),(random.randrange(0,2),random.randrange(0,2),random.randrange(0,2),random.randrange(0,2)))

print(a.make_T_list()[0])
'''
