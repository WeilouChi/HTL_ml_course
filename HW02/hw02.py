import random
import numpy as np

def sign(x, theta_value):
    t = []
    for i in range(len(x)):
        tem = x[i] - theta_value
        if tem > 0:
            t.append(1)
        else :
            t.append(-1)
    return np.array(t)

def generate_data(size, noise):
    x = np.zeros((size, 1))
    y = np.zeros((size, 1))
    for i in range(size):
        x[i][0] = random.uniform(-1,1)
        ran = random.uniform(0,1)
        if ran < noise:
            y[i][0] = -sign(x[i],0.0)
        else:
            y[i][0] = sign(x[i],0.0)
    return x, y

def get_theta(x,size):
    
    tem = np.sort(x[:,0])
    theta = np.zeros((size,1))
    for i in range(size-1):
        theta[i] = (tem[i]+tem[i+1])/2
    theta[-1] = -1
    return theta

def decision_stump1(size, noise):
    e_in = 1
    x, y = generate_data(size, noise)
    theta = get_theta(x, size)
    for i in theta[:,0]:
        dif_pos = np.where(x[:,0]>i,1,-1)
        dif_neg = np.where(x[:,0]<i,1,-1)
        err_pos = sum(dif_pos != y[:,0])
        err_neg = sum(dif_neg != y[:,0])
        print(err_pos, err_neg)
        err_pos /= size
        err_neg /= size
        if err_pos > err_neg:
            if e_in > err_neg:
                e_in = err_neg
                s = -1
                best_theta = i
        else:
            if e_in > err_pos:
                e_in = err_pos
                s = 1
                best_theta = i
        #print(e_in)
    return e_in, best_theta, s

def problem(size,noise):
    sum_ein = 0
    sum_eout = 0
    for i in range(10000):
        e_in, best_theta, s = decision_stump1(size, noise)
        sum_ein += e_in
        if s == 1:
            sum_eout += abs(best_theta)/2 * (1 - noise) + noise * (1 - abs(best_theta)/2)
        else:
            sum_eout += abs(best_theta)/2 * (noise) + (1 - noise) * (1 - abs(best_theta)/2)
            
    return sum_ein/10000, sum_eout/10000,  sum_eout/10000 -sum_ein/10000

print(problem(2,0))
print(problem(20,0))
print(problem(2,0.1))
print(problem(20,0.1))
print(problem(200,0.1))