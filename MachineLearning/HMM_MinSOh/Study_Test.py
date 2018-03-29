from Study_Model import Learner


######################################################
#################### 4.Examples ######################
######################################################

asset_list = [2, 3, 1, 2, 3, 2, 5]

ActivitySet = [[(0, 0, 2), (0,), (2, 2), (2, 0, 0), (2, 1), (2, 2, 2, 2, 2)], #이해를 잘하지만, 문제를 잘 안푸는 학생
               [(0, 1, 2), (2,), (2, 0), (2, 2, 0), (2, 1), (2, 1, 2, 2, 0)], #이해도가 중간 정도인 학생
               [(2, 2, 2), (2,), (2, 0), (2, 2, 0), (2, 1), (2, 2, 2, 2, 0)], #아주 뛰어난 학생
               [(0, 1, 2), (1,), (1, 2), (1, 2, 0), (0, 1), (2, 0, 1, 0, 1)]] #이해도가 낮은 학생

a = [Learner(asset_list) for i in range(len(ActivitySet))]
for i in range(len(ActivitySet)):
    a[i].initialize()

for i in range(len(ActivitySet)):
    print('######################################################')
    print('#####################Table ' + str(i+1)+ '##########################')
    print('######################################################')
    for j in range(len(ActivitySet[i])):
        print('Activity in step ' +str(j+1) +':'+ str(ActivitySet[i][j]))
        a[i].activity(j+1,ActivitySet[i][j])
        print('Evaluation: '+ str(a[i].analyze_all()))