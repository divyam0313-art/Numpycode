## Basic arithmatic +,-,*,/
import numpy as np

from numpy import random as rng

nparray1=np.array([1,3,6,9])
nparray2=np.array([3,5,87,2])
nparray3=np.array([[2,2,2,2],[3,3,3,3]])


print("add", np.add(nparray2,nparray1))
print("addition ",nparray2+nparray1)
print("-", np.subtract(nparray2,nparray1))
print("*", np.multiply(nparray2,nparray1))
print("/", np.divide(nparray2,nparray1))
print("add", np.multiply(nparray3,nparray1))


## LOGaRITHMIC
nplogarray=np.array([1,np.e,100])

print ("natural log with base e", np.log(nplogarray))
print ("natural log with base 2", np.log2(nplogarray))
print ("natural log with base 10", np.log10(nplogarray))
print ("np{e}, np.exp{1}", np.e ,"expo" , np.exp(1))

## exponent and power

nppowerarray=np.array([1,2,3,4])

print("power 2",np.power(nppowerarray,2))
print("exponent",np.exp(nppowerarray))


 ## TRIGONOMETRIC
nptrigarray= np.array([0,np.pi/2,np.pi])

print("sin func is", np.sin(nptrigarray))
print("cos func is", np.cos(nptrigarray))
print("tan func is", np.tan(nptrigarray))
print("tan func is", np.cosh(nptrigarray))


## absolute functions
## abs,sign,round,floor,ceil,trunc

mpfloatarray=np.arange(-2.43,5,1.2)
print(mpfloatarray)
print("floor is",np.floor(mpfloatarray))


## logical nd universal

## less[each element of a less than b],less_equal,greater,np.logical_and

a=np.array([1,2,3,4])
b=np.array([2,3,4,5])
print(np.less(a,b))
cond1=a>3
cond2=b<3
print(np.logical_and(cond1,cond2))

## statistival sum,mean,variance,standard deviation,min,max,Argmin(index of min),median,Quantile

npstatarray=np.array([[1,2,3],[2,5,6],[2,5,7],[7,6,5]])

print("sum of all elements",np.sum(npstatarray))

print("print sum of all rows,rows axis=1,columns axis=0",np.sum(npstatarray,axis=1))

## broadcasting
## mathoperations b/w 2 different shape arrays
npbroadarray1=np.array([1,2,3])
print("creates an array of 10 with same simention of input and adds",npbroadarray1+10)
npbroadarray2=np.array([[10],[20],[30]])
print(npbroadarray1+npbroadarray2)

## linear Algebra
la1=np.array([[1,2],[3,4]])
la2=np.array([[5,6],[7,8]])
print("a multipy b adot(b) or a@b  or np.matmul(A,B)", la1.dot(la2))

print("inverse,determinant", np.linalg.inv(la1),np.linalg.det(la1))

## Random module: generate random nums

tandomarray1= np.random.random_integers(20,50,4)
print(tandomarray1) 
