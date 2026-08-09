import numpy as np
rng= np.random.default_rng(seed = 42)

array1=[1,2,3,4,5,6,7,9,8]
numpyarray1=np.array(array1)
print("numpy array is :", numpyarray1)

numpyarray2=np.zeros((2,5))
print("numpy array2 is :", numpyarray2)

numpyarray3=np.arange(2,stop=12,step=2)

print("numpy array3 is :", numpyarray3)

numpyarray4=np.linspace(start=2,stop=14,num=10)

print("numpy array4 is :", numpyarray4)

print(f"element at index 3 is {numpyarray1[3]}")

print(f"slice array at indices 2,8 with step 2 is {numpyarray1[2:8:2]}")

nparray5=np.array([[1,2,3],[13,4,5],[15,6,7],[18,9,10]])
print(f"multidimension array is {nparray5}")

print(f"element at index 2,3 is {nparray5[1,2]}")

print(f"slice rows 0 to 2 and column 0 to 1 is {nparray5[0:2,0:1]}")

print(f"slice rows 0 to 2 and all colums is {nparray5[[0,2] ,:]}")

## BOOLEAN INDEXING

mask= nparray5 > 5
print (mask)
print (nparray5[mask])

## RESHAPE

print(nparray5.reshape(6,2))

## Ravel (flatten)

ravel= nparray5.ravel("C")
print(f"ravelled data is {ravel}")

## tRANSPOSE  expose rows and colums

print(nparray5.transpose())

## DATA Types

nparray6=np.arange(1.3,6.5,1.3)
print (f"nparray6  is {nparray6}")
print("datatype of nparray6 is ",nparray6.dtype)

## change float to int

intnparray=nparray6.astype(np.int64)
print("intnparray is",intnparray)
