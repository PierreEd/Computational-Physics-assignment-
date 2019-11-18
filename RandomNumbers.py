#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 16:19:22 2018

@author: jacquetpierreedouard
"""

import numpy as np 
import matplotlib.pyplot as plt
import time 

n=10**6
Z0=1


#pseudo random number generator, here a linear congruential generator 
def LCG(n,ymax, Z0):
    a=78279178895
    b=54321
    c=2**30
    X=np.zeros(n)
    z=Z0
    for i in range(n):
        z=(z*a+b)%c
        X[i]=z
    return(X*ymax/c)
    
#def of the desired pdf(x) for question b) 
def pdf(x):
    valF=np.sin(x)/2
    return(valF)

#def of the cumulative distribution function (cdf) associated to pdf(x)         
def cdf(x):
    valC=(1-np.cos(x))/2
    return(valC)
    
#def of the inverse of the cdf 
def cdfin(x):
    valI=np.arccos(1-2*x)
    return(valI)
    
  
#def of the desired pdf(x) for question c)   
def pdf2(x):
    val2=2*(np.sin(x)**2)/np.pi
    return (val2)
#comparison function useful in question c), pdf2(x) is smaller than compF(x) for all x 
def compF(x):
    return(1.3*pdf(x))


#question a) uniformly distributed random numbers 
#set bol(n) to 1 to have it plot something 
bol1= 1
if bol1==True:
    X=LCG(10**5,1,1)
    plt.hist(X, bins=40,color='darkgray',edgecolor='black', linewidth=1.2,label='histogram of 10^5 uniformely distributed data points ')
    plt.grid()
    plt.ylim(0,3000)
    plt.xlabel('x')
    plt.ylabel('number of samples')
    plt.title('Uniformly generated numbers in range [0,1]')
    plt.legend()
    
    plt.show()



#I didn't cover the time task in my report but I did include it in my code, I just didn't have 
#much time
#to see the ratio of time taken both bol2 and bol3 need to be on, i.e. =1 otherwise dtTrans is not calculated 


    
#question b) random numbers following pdf1() // Transformation method 
bol2= 0
if bol2==True: 
    t_ini=time.time() 
    Y=cdfin(LCG(10**5,1,1))
    t_f=time.time()
    #time taken to compute all x values
    dtTrans=t_f-t_ini
    plt.hist(Y,normed=True, bins=40,color='darkgray',edgecolor='black', linewidth=1.2,label='histogram of randomly generated data ')
    plt.grid()
    plt.ylim(0, 0.6)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('P(x) using transformation method ')
    plt.legend()
    plt.show()
    
#question b) random numbers following pdf2() // Accept-Reject Method
bol3=0
if bol3==True:  
    #generate random values following pdf1
    X=cdfin(LCG(10**5,1,1))
    x=np.array([])
    P=np.array([])
    t_ini=time.time() 
    
    for i in range(len(X)):
        #generate random number in range 0 to compF(x)
        p=np.random.uniform(0,compF(X[i]))
        if pdf2(X[i]) > p:
            #accept if an only if the X in question is situated between p and compF(x)
            x=np.append(x,X[i])
            P=np.append(P,p)
    t_f=time.time()
    #time taken to compute all x values
    dtAcc=t_f-t_ini
    print('time taken to compute y with transformation method',dtAcc)
    print('time taken to compute y with accept/reject method',dtTrans)
    print('ratio of time taken',dtAcc/dtTrans)
    plt.hist(x, normed=True, bins=40,color='darkgray', edgecolor='black', linewidth=1.2,label='histogram of randomly generated data')
    plt.plot(x,compF(x), 'r.',label='comparison function')
    plt.plot(x,pdf2(x), 'k.', label='predicted pdf')
    plt.legend()
    plt.title('P(x) using rejection method ')
    plt.grid()
    plt.xlabel('x')
    plt.ylabel('y')        
    plt.show()
    
    
