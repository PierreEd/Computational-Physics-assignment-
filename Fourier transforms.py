#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 11:37:05 2018

@author: jacquetpierreedouard
"""



import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack 
from scipy import signal

#T return the time step given the limits and the number of samples we want 
def T(a,b,n):
    v=(b-a)/n
    return(v)
    
#def of f being step function over range [-5,5]
def h(x):
    if x<3 or x>5:
        val=0
    else:
        val=4
    return (val)

#def of g being a gaussian centered around 0 
def g(x):
    val=np.exp(-(x**2)/2)/((2*np.pi)**0.5)
    return (val)

#def function that returns X, H and G as arrays of n numbers ranging from a to b f
def sample(a,b,n):
    #create empty array for X, F and G
    X=np.linspace(a,b,n)
    H=np.zeros(n)
    G=np.zeros(n)
    for i in range(n):
        H[i]=h(X[i])
        G[i]=g(X[i])
    
    return(X,H,G)
    
# def of the convolution   
def ProdConv(a,b,n):
    (X,H,G)=sample(a,b,n)
    #first we need X, H  and G as arrays to be able to perform operations on them 
    #we pad H and G on the left and right, changing them into arrays on length 13*n
    H=np.pad(H,(6*n,6*n),'constant')
    G=np.pad(G,(6*n,6*n),'constant')
    #create empty array of same dimensions
    HG=np.zeros(len(H))
    #compute FFT for H and G 
    HFFT=np.fft.fft(H)
    GFFT=np.fft.fft(G)
    HG=HFFT*GFFT
    #get back to the x-domain by using ifft() multiplied by the time step 
    convHG=np.fft.ifft(HG,len(HG))*T(a,b,n)
    #X needs to match the values taken by convHG so we make it bigger, array of 13*n values 
    X=np.linspace(a-6*n*T(a,b,n),b+6*n*T(a,b,n),len(HG))
    #need to shift the X array to recenter it 
    Xshift=np.fft.ifftshift(X)
    return(Xshift, convHG)

#setting lower bound, higher bound, and number of samples (power of 2 to optimize FFT)
a=-10
b=10
n=2**8
(X,H,G)=sample(a,b,n)
(Xs,HG)=ProdConv(a,b,n)
(P1,P2,P3)=(plt.plot(X,H, 'b.',label='h(x)'),plt.plot(X, G, 'k.',label='g(x)'), plt.plot(Xs, np.real(HG), 'r.',label='h*g(x)' ))
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.xlim(a,b)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Plot of h(x),g(x) and their convolution')
plt.grid()
plt.show()
