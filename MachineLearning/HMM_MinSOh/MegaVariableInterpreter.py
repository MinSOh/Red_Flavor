class interpreter:
    def __init__(self,shape_tuple):
        '''
        Let MegaVariable M = (X_0, ... , X_n-1)
        :param list: [a_0, a_1, ... ,a_n-1]
        a_0 = |X_0| , ... , a_n-1 = |X_n-1|
        If (X_0, ... , X_n-1) = (i_0, ... , i_n-1),
        we change this MegaVariable to integer s.t.
        i_
        '''
        self.shape = shape_tuple

    def get_shape(self):
        return self.shape

    def tuple_to_int(self,tuple):
        if len(self.shape) != len(tuple):
            print('[Error] [Interpreter:tuple_to_int] input tuple length must be '+str(len(self.shape)))
            return None
        else:
            exp = 1
            result = 0
            l = len(tuple)
            for i in range(l):
                j = l-1-i
                temp = self.shape[j]
                if tuple[j]<temp:
                    result = result + exp*tuple[j]
                else:
                    print('[Error] [Interpreter:tuple_to_int] '+str(j)+'\'s element of input tuple is out of bound')
                    return None
                exp = exp*temp
            return result

    def int_to_tuple(self,integer):
        maxi = 1
        for i in range(len(self.shape)):
            maxi = maxi*self.shape[i]
        if integer < maxi:
            l = len(self.shape)
            result = [0]
            result = result*l
            remainder = integer
            for i in range(l):
                j = l-1-i
                temp = remainder%self.shape[j]
                result[j] = int(temp)
                remainder = (remainder - temp)/self.shape[j]
            return tuple(result)


        else:
            print('[Error] [Interpreter:int_to_tuple] Input integer must be smaller than '+str(maxi))
            return None