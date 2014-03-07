import numpy as np
import matplotlib.pyplot as plt




def lamb_0(X):
    return 1E-2

def lamb_1(X):
    
    M = X[0]
    
    return M*5E-3

def lamb_2(X):
    
    M = X[0]
    
    return M*1E-3

def lamb_3(X):
    
    Z = X[1]
    
    return Z*1E-4


def sample_wait_time(X, sum_of_rates):
    
    M, Z = X
    
    scale =  sum_of_rates
    
    wait_time = np.random.exponential(scale)
    
    return wait_time
    
def choose_reaction_type(rates_list, sum_of_rates):
    
    P = [(rate/sum_of_rates) for rate in rates_list]
    
    random_number = np.random.uniform()
    
    for i in range(4):
        if random_number <= sum(P[0:i+1]):
            reaction_type = i
            return reaction_type
        else:
            continue
    
    print "error in choosing reaction type"
    
    
def two_stage_process(iterations, X0, S, rates_list):
    
    X = X0.copy()
    t = 0
    
    T = []
    X_list = []
    
    T.append(t)
    X_list.append(X)
    
    for i in range(iterations):
        
        rates_x = [rate(X) for rate in rates_list]
        sum_of_rates = sum(rates_x)
        
        t += sample_wait_time(X, sum_of_rates)
        reaction = choose_reaction_type(rates_x, sum_of_rates)
        X_new = X + S[:,reaction]
        
        T.append(t)
        X_list.append(X_new)
        
        X = X_new
        
    T = np.array(T)
    X_list = np.array(X_list)
    
    return T, X_list
    
    
    
        
rates_list = [lamb_0, lamb_1, lamb_2, lamb_3]
S = np.array([1.,0.,-1.,0.,0.,1.,0.,-1.]).reshape(2,4)

T, X_list = two_stage_process(10, np.zeros(2), S, rates_list)
    