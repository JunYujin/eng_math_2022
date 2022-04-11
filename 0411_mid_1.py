import numpy as np
def equationToMat():
    n = int(input()) # number of equations
    A, B = np.full((n, n), 0), np.full((n, 1), 0)
    for i in range(n) :
        strEq = input() # equation : ex) 2x1 - x2 + 5x3 + x4 = -3
        
        #code here
    return A, B 

A, B = equationToMat()
print("Matrix A = ", A)
print("Vector B = ", B)
