#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 13:24:57 2018

@author: jacquetpierreedouard
"""
import numpy as np 
#def a function that from an input n*n matrix will return 2 n*n matrices
#L is a lower triangular matrix whose diagonal entries are normalized to 1 
#U is a upper triangular matrix
def LUdec(A):
    n=len(A)
    #create empty matrices of appropriate zise
    L=np.zeros((n,n))
    U=np.zeros((n,n))
    #Need to perform Crout's Algorithm to get the L[i,j] and U[i,j] components 

    for i in range(n):
        #normalise diagonal entries of L 
        L[i, i] = 1.0
        for j in range(i+1): 
            #from 0 to i (fun range goes from 0 to i) since s0 needs to be summed for s from 0 to i
            s0 = sum(U[s, i]*L[j, s] for s in range(j)) 
            #need to sub s0 to the associated A[i,j] value 
            U[j, i] = A[j, i] - s0
        for j in range(i, n):
            #from i to n since s0 needs to be summed for s from 0 to j+1
            s1 = sum( U[s, i]*L[j, s]  for s in range(j))
            L[j, i] = (A[j, i] - s1) / U[i, i]   
    #we want the results as a single matrix with non diagonal l_ij and all u_ij 
    D=np.zeros((n,n))
    
    for j in range (n):
        #now just overwriting the matrix 
        for k in range(n):
            if j!=k:
                D[j,k]=U[j,k]+L[j,k]
            else:
                D[j,k]=U[j,k]
                
    return (L,U,D)


#def a function that returns the solution to the linear system Ax=LUx=b using back and forward sub
def BFSub(L,U,b):
    n=len(L)
    #create 2 empty vectors of lenght n to solve Ax=b in two step, Ly=b then Ux=y
    y=np.zeros((n,1))
    x=np.zeros((n,1))
    y[0]=b[0]/L[0,0]
    for i in range (1,n):
        #forward substitution / finding the y[i]
        S0=sum(L[i,s]*y[s] for s in range(i)) #summing from 0 to i
        y[i]=b[i]-S0 #dividing by 1 (l[i,i])
    for j in range (n-2,-1,-1): #so that the order of terms calculated is from N-2 down to 0 (N-2,N-3,N-4,...,2,1,0)
        #backward substitution / finding the x[i] from the y[i]]
        x[n-1]=y[n-1]/U[n-1,n-1]
            
        S1=sum(U[j,t]*x[t] for t in range(j+1,n)) #summing from j+1 to n, this terms are known since i goes from N-2 to 0 
        x[j]=(y[j]-S1)/U[j,j]
              
    return(x)
    

 
A=np.array([[3,1,0,0,0],[3,9,4,0,0],[0,9,20,10,0],[0,0,-22, 31, -25],[0,0,0,-55,60]])
b=np.array([[ 2],[ 5],[-4],[ 8],[ 9]])
n=len(A) 
(L,U,D)=LUdec(A)

#Code for question a), b) and c) , set bol(n) to 1 to get it working, otherwise 0 
bol1=0
if bol1==1:
    det=np.linalg.det(A)    
    DET0=1
    for k in range(0,n):
        DET1=U[k,k]*DET0
        DET0=DET1 
    print('low triangular matrix L:','\n', L) 
    print('high trianguar matrix U:' ,'\n', U)
    print('matrix of coefficient D:','\n' ,D)
    print('determinant calculated from U is', DET0,'\n','determinant calculated from inbuilt function is:',det)
    


#this one is just a validation    
bol2=0
if bol2==1:
    print('matrix product of L and U:','\n',np.matmul(L,U),'\n','original matrix A:','\n',A)
    
bol3=0
if bol3==1:
    x=BFSub(L,U,b)
    print('solution to matrix equation is:','\n',x)

#same here, just checking that Ax=b
bol4=0 
if bol4==1: 
    c=np.matmul(A,BFSub(L,U,b))
    print(c)

#find the inverse of A
bol5=0
if bol5==1:
    I=np.identity(n)
    X=np.zeros((n,n))
    for i in range(0,n):
        #needs to be reshaped since BFSub takes 2 matrices and a column vectors as arguments 
        x=BFSub(L,U,I[:, i].reshape((-1, 1)))
        x=np.reshape(x,[n])
        #now just overwrite the empty matrix X
        X[:,i]=x
    print('Inverse of A is: ',X)
    
    print('The product of A by the computed inverse is:',np.matmul(A,X))
    
   

      