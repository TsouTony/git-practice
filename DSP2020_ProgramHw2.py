import pandas as pd
import numpy as np
from numpy.linalg import inv

#k : sparsity
#X : test data, n*d
#B : basis for selection, n*m
def OMP(k, X, B):
    slt_idx = np.zeros((X.shape[1], k))
    slt_basis = np.zeros((X.shape[1], k, X.shape[0]))
    r = X
    for i in range(k):
        print("i = ",i)
        # (m*n) * (n*d) = (m*d), vectoried
        slv_max = np.dot(B.transpose() , r)
        max_idx = slv_max.argmax(axis = -1)
        for j in range(X.shape[1]):
            print("j = ",j)
            slt_idx[j, i] = max_idx[i]
            #slt_basis : i*n
            slt_basis[j, 0:i] = B.transpose()[slt_idx[j, 0:i], :]
            #X[:,j] : n*1, c : i*1
            c = np.dot(np.dot(inv(np.dot(slt_basis, slt_basis.transpos())) , slt_basis), X[:, j])
            r[j]  = X[j] - np.dot(slt_basis.transpose(), c)
            
    return slt_basis
        

if __name__ == "__main__":
    data_csv_train = pd.read_csv('mnist_train.csv')
    data_train = data_csv_train.values
    data_csv_test = pd.read_csv('mnist_test.csv')
    data_test = data_csv_test.values
    #X_train : n*m1(60000)
    #X_test : n*m2(10000)
    X_train = data_train[:,1:].transpose()
    X_test = data_test[:,1:].transpose()

    #ans = OMP(5, X_test[:, 0:1000], X_train)
