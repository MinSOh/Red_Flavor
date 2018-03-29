import numpy as np
import helper

class Learn:
    def __init__(self,t,m,n,history=None):
        '''

        :param t:
        :param m: t+1일때의 state
        :param n: t일떄의 state
        :param history:
        '''
        self.t = t
        self.m = m
        self.n = n
        self.history = history
    def initialize(self):
        self.history = np.zeros((self.m,self.n))
        return self.history
    def get_m(self):
        return self.m
    def get_n(self):
        return self.n
    def get_history(self):
        return np.reshape(self.history,(self.m,self.n))
    def ingest(self,m,n,delta=1):
        self.history[m][n] = self.history[m][n] + delta
        return self.history
    def ingest_as_list(self,list):
        for i in range(len(list)):
            self.ingest(list[i][0],list[i][1])
    def make_transition_model(self):
        return helper.column_normalize(self.history)

'''
A = Learn(0,5,4)
A.initialize()
print(A.get_history())
print(A.get_m())
print(A.get_n())
A.ingest(0,0)
A.ingest(1,2,3)
A.ingest(2,1,1)
A.ingest(3,0,2)
A.ingest(3,2,7)
A.ingest(4,1,3)
print(A.get_history())
print(A.make_transition_model())

B = Learn(0,5,4)
B.initialize()
makelist = []
for i in range(100):
    makelist.append([(i*i+random.randrange(0,100))%5,(i*i*i+random.randrange(0,100))%4])
B.ingest_as_list(makelist)

print(B.get_history())
print(B.make_transition_model())
'''

