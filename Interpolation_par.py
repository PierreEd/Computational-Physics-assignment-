#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 13:24:55 2018

@author: jacquetpierreedouard
"""

import numpy as np
import matplotlib.pyplot as plt
from LUdecomposition import BFSub, LUdec
from itertools import repeat


# def of 4 functions calcultating the 4 members of the equation between point x[j] and  x[j+1]
def calc_s1(z, X, x, h, j, i):
    return z[j+1]*((X[i]-x[j])**3)/(6*h[j])

def calc_s2(z, X, x, h, j, i):
    return z[j]*((x[j+1]-X[i])**3)/(6*h[j])

def calc_s3(z, X, x, h, j, y, i):
    return ((y[j+1]/h[j])-(z[j+1]*h[j]/6))*(X[i]-x[j])

def calc_s4(z, X, x, h, j, y, i):
    return ((y[j]/h[j])-(h[j]*z[j]/6))*(x[j+1]-X[i])

#def of a function that from 2 arrays of same size returns a plot of the piecewise linear model associated to it 
def LinInt(x,y):
    for i in range(len(x)-1):
        a=y[i+1]-y[i]
        b=x[i+1]-x[i]
        #discretization of the x-axis between data points x[j] and  x[j+1]
        X=np.linspace(x[i],x[i+1])
        Y=np.zeros(len(X))
        for j in range(len(X)):
            #equation of a line/ Y coordinates associated to the X 
            Y[j]=(a*(X[j]-x[i])/b)+y[i]
        plt.plot(X,Y, "b")
        plt.plot(x[i], y[i], "ok",)
        plt.plot(x[i+1], y[i+1], "ok")

#def of a function that returns a plot of the cubic interpolation of the two input arrays (same size once again)
def CubicInt(x,y):
    n =len(x)-1
    h=np.zeros(n)
    dy=np.zeros(n)
    v=np.zeros(n-1)
    u=np.zeros((n-1,1))
    S=np.zeros((n-1,n-1))
    #def of convenient arrays h[],dy[], v[] and u[]
    for i in range(n):
        h[i]=(x[i+1]-x[i])
        dy[i]=(y[i+1]-y[i])/h[i]

    for j in range(n-1):  
        v[j]=2*(h[j+1]+h[j])
        u[j,0]=6*(dy[j+1]-dy[j])
    
    #initializing the top left value of the matrix 
    S[-1,-1]=v[-1]
    for k in range(n-2):
        #overwrite the matrix 
        S[k,k]=v[k]
        S[k,k+1]=h[k]
        S[k+1,k]=h[k]

      
    (L,U, D)=LUdec(S)
    
    z=BFSub(L,U,u)
    #need to include z_0 and z_n both equal to zero (natural cubic spline) 
    z=np.insert(z,0,0)
    z=np.append(z,0)

    for j in range(n):
        X=np.linspace(x[j],x[j+1],50)
        #use of the repeat() function to calculate all the S1 in parallel 
        #can think of S1, S2, S3, S4 as vectors on which others functions (calc_si) are acting 
        S1 = np.array(list(map(calc_s1, repeat(z), repeat(X), repeat(x), repeat(h), repeat(j), range(len(X)))))
        S2 = np.array(list(map(calc_s2, repeat(z), repeat(X), repeat(x), repeat(h), repeat(j), range(len(X)))))
        S3 = np.array(list(map(calc_s3, repeat(z), repeat(X), repeat(x), repeat(h), repeat(j), repeat(y), range(len(X)))))
        S4 = np.array(list(map(calc_s4, repeat(z), repeat(X), repeat(x), repeat(h), repeat(j), repeat(y), range(len(X)))))
        Y= S1 + S2 + S3 + S4
        #Y features all the data points from i=0 to i=n
        
        plt.plot(X,Y,'r')
        plt.plot(x[j], y[j],'ok')
        plt.plot(x[j+1], y[j+1],'ok')

    

#define X and Y data set to perform interpolations on them 
X=np.array([-2.1,-1.45,-1.3, -0.2, 0.1, 0.15, 0.8, 1.1, 1.5, 2.8,3.8]  ) 
Y=np.array([0.012155, 0.122151, 0.184520, 0.960789, 0.990050, 0.977751, 0.527292, 0.298197,0.105399, 3.936690e-4,5.355348e-7])      
LinInt(X,Y)
CubicInt(X,Y)   
plt.xlabel('x')
plt.ylabel('y')
plt.title('Cubic interpolation of input data (x,y)')
plt.title('Interpolations')
plt.grid()
plt.show()     


 
        