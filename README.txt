{\rtf1\ansi\ansicpg1252\cocoartf1561\cocoasubrtf100
{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 Python is a good language for this exercise although I believe C or C++ would have been more adequate for the random numbers part (more optimised maybe).\
I really tried to write concise and efficient algorithm, I parallelised the operations in the Cubic Spline task as all values could be computed independently once the column vector featuring the second derivatives was known. \
\
For parts II, III, IV and V, the \'91bol1\'92, \'91bol2\'92, etc\'85 act as switch, set them to 0 or false and they won\'92t display anything, but set them to 1 and you\'92ll \'91turn\'92 them on:\
\
\
PART I:\
just run the script\
\
PART II: \
a) \
\
b) set bol1=1 to return L,U, D and print the determinant (bol2=1 is a validation, it prints the matrix product of L and U)\
\
c) \
\
d) set bol3=1 to return the solution to the matrix equation with b given in the assignment paper  (bol4=1 is a validation too, it just prints np.matmul(A,x) to check wether we recover the same b)\
\
e) set bol5=1 to return the computed inverse of A called X, the validation of that one is directly on the same boolean and it prints np.matmul(A,X) to check if we find the identity matrix back \
\
PART III:\
just run the script \
\
PART IV:\
just run the script ( you can change the values for a, b and n if you want) \
\
PART V:\
a) set bol1=1 to plot the uniformly  distributed x\
\
b) set bol2=1 to compute and plot pdf1 via transformation method \
\
c) set bol3=1 to compute and plot pdf2 via accept/reject method\
\
}