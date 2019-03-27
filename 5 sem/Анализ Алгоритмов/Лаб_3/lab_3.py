from math import factorial

n = 5                                   #0
nach = 0                                #1
m = 6                                   #2
x = 2                                   #3
t=x                                     #4
k = 1                                   #5
temp = 1                                #6
z = x                                   #7

while abs(t)> 0.1 and k<m:              #8
    
    nach+=n                             #9
    k+=1                                #10

    temp = temp * (k*2-3)               #11 
    ch = temp * x**(k*2-1)              #12 
    zn = factorial(k*2-1)/(temp)        #13

    t = (-1)**k * ch/zn                 #14

    z += t                              #15

