#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 15:51:12 2018

@author: jacquetpierreedouard
"""
import numpy as np

#Store 1 as a double floating point using np.float64()
a = np.float64(1)  
#Need to define explicitely so that the quotient epsilon64/np.float64(2) is itself a double floating point          
epsilon64=np.float64(1)       
epsilon64_last=np.float64()  

while a + epsilon64 != a :
    epsilon64_last = epsilon64
    epsilon64 = epsilon64/np.float64(2) 
    #divide systematically by 2 to get epsilon as it has to be a power of 2  
    

#Same but for single floating points i.e. 32bits
b = np.float32(1)
epsilon32=np.float32(1)
epsilon32_last=np.float32()

while b + epsilon32 != b :
    epsilon32_last = epsilon32
    epsilon32 = epsilon32/np.float32(2)

#Same but for extended floating points i.e. 128bits
c = np.float128(1)
epsilon128=np.float128(1)
epsilon128_last=np.float128()

while c + epsilon128 != c :
    epsilon128_last = epsilon128
    epsilon128 = epsilon128/np.float128(2)

print ('error 128bits :',epsilon128_last, '\n','error 64bits :',epsilon64_last, '\n','error 32bits :',epsilon32_last  )


