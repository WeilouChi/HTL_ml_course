import random
import numpy as np

def get_data(size, noise):
    x = np.zeros((size,1))
    y = np.zeros((size,1))
    for i in range(size):
        x[i] = random.uniform(-1,1)
        ran = random.uniform(0,1)
        if ran < noise:
            y[i] = -np.sign(x[i])
        else:
            y[i] = np.sign(x[i])
    return x, y   

def decison_stump_DP(size, noise, x, y, N=0, e_in=1, best_theta=0, s=0):  
    tem = np.sort(x[:,0])  
    
    if N == size - 1:
        theta = -1
    else:
        theta = (tem[N] + tem[N+1]) / 2
    pos = np.where(x[:,0] > theta,1,-1)
    neg = np.where(x[:,0] > theta,-1,1)
    err_pos = sum(pos !=y [:,0])
    err_neg = sum(neg !=y [:,0])
    err_pos /= size
    err_neg /= size
    
    if err_pos > err_neg:
        if e_in > err_neg:
            e_in = err_neg
            s = -1
            best_theta = theta
    else:
        if e_in > err_pos:
            e_in = err_pos
            s = 1
            best_theta = theta
    
    
    if N == size - 1:
        return e_in, best_theta, s

    return decison_stump_DP(size, noise, x, y, N+1, e_in, best_theta, s)

def problem(size, noise):
    sum_Ein = 0
    sum_Eout = 0

    for i in range(10000):
        x, y = get_data(size, noise)
        e_in, best_theta, s = decison_stump_DP(size, noise, x, y)
        sum_Ein += e_in
        if s == 1:
            sum_Eout += abs(best_theta)/2 * (1 - noise) + noise * (1 - abs(best_theta)/2)
        else:
            sum_Eout += abs(best_theta)/2 * (noise) + (1 - noise) * (1 - abs(best_theta)/2)
        
    return sum_Ein/10000, sum_Eout/10000,  sum_Eout/10000 - sum_Ein/10000

#16
print(problem(2,0))
#17
print(problem(20,0))
#18
print(problem(2,0.1))
#19
print(problem(20,0.1))
#20
print(problem(200,0.1))