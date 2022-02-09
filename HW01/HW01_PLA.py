import numpy as np
import random
import matplotlib.pyplot as plt

def loadfile(x0):
    with open('hw1_train.txt','r') as dat:
        lines = dat.readlines()
    
    xn = []
    yn = np.zeros((len(lines),1))
    i = 0
    for line in lines:
        tem = line.split()
        x = [x0] + [np.float(i) for i in tem[:-1]]
        xn.append(x)
        yn[i] = np.float(tem[-1])
        i += 1

    return np.array(xn), yn

def sign(x):
    if x <= 0:
        return -1
    else:
        return 1
    
def PLA(xn, yn, w, lr):
    count = 0
    n = len(xn)
    correct = 0
    flag = True
    while True:
        flag = True
        num = range(n)
        randpick = random.choices(num, k=5*n)
        for j in range(5*n):
            if sign(np.dot(xn[randpick[j]], w)[0]) != yn[randpick[j],0]:
                correct = 0
                w += lr * yn[randpick[j],0] * np.matrix(xn[randpick[j]]).transpose()
                flag = False
                break
            else:
                correct += 1
            if correct == 500:
                break
                
        count += 1    
        if correct == 500:
            break
    return flag, count, w

def question(x0, n):
    xn, yn = loadfile(x0)
    
    lr = 1
    updatas = []
    wzero = []
    for _ in range(n):
        w0 = np.zeros((11,1))
        flag, count, w = PLA(xn, yn, w0, lr)
        if flag:
            updatas.append(count)
            wzero.append(w[0][0])
#     print(con)
#     print(wzero)
#     plt.hist(updatas)
#     plt.show()
#     plt.close()
#     plt.hist(wzero)
#     plt.show
    
    
    return int(np.median(updatas)), int(np.median(wzero))

print(question(1, 1000))