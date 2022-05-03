#!/usr/bin/env python
# coding: utf-8

# In[8]:


### import numpy as np
def equationToMat():
    n = int(input()) # number of equations
    A, B = np.full((n, n), 0), np.full((n, 1), 0)
    for i in range(n) :
        strEq = input() # equation : ex) 2x1 - x2 + 5x3 + x4 = -3
        cut= strEq.split() #strEq를 공백기준으로 자르기
        B[i,0]=cut[-1] #-1은 마지막 숫자를 의미
        length = len(cut)
        for z in range(1,length-2,2):  #연산자를 뒤에 있는 값에 넣기
            cut[z+1]=cut[z]+cut[z+1]   
        for j in range(0,length-2,2): #필요없는 연산자는 취급 X
            cut1=cut[j].split('x')  # cut을 x를 기준으로 자르기
            if(cut1[0]=='-'):
                cut1[0]=-1
            if(cut1[0]=='' or  cut1[0]=='+'):
                cut1[0]=1
            A[i,int(cut1[1])-1]=  cut1[0] # 문자열을 정수형으로 변환
                                          # i = 열을 의미 int(cut1[1])-1 = 행을 의미
            
        #code here
    return A, B 

A, B = equationToMat()
print("Matrix A = ", A)
print("Vector B = ", B)


# In[ ]:


2x1 - x2 + 5x3 + x4 = -3
3x1 + 2x2 + 2x3 - 6x4 = -32
x1 + 3x2 + 3x3 - x4 = -47
5x1 - 2x2 - 3x3 + 3x4 = 49

