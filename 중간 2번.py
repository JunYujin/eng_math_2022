#!/usr/bin/env python
# coding: utf-8

# In[14]:


import numpy as np
def printMatrixTypes(A) :
       n,m=A.shape
       if(n!=m):
           return ("정방행렬이 아니다.")
       else:
           if(n==2):
               if(A[0,0]*A[1,1]-A[0,1]*A[1.0] !=0):
                    print(np.linalg.inv(A))
               if(np.array_equal(A,np.triu(A))):
                    return ("상삼각행렬이다.")
               if(np.array_equal(A,np.tril(A))):
                    return("하삼각행렬이다.")
               if(np.array_equal(A,np.eye(n))):
                    return("단위행렬이다.")
           else:
               return("정방행렬이다.")
       pass

A = np.array([[3, 0], 
             [-1, 2],
             [1, 1]])
print("Matrix A = ", printMatrixTypes(A))


# In[ ]:


2x1 - x2 + 5x3 + x4 = -3
3x1 + 2x2 + 2x3 - 6x4 = -32
x1 + 3x2 + 3x3 - x4 = -47
5x1 - 2x2 - 3x3 + 3x4 = 49

