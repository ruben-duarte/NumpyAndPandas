import numpy as np

#initialize an array

a = np.array([1, 2, 3])
a = np.array([1, 2, 3], dtype= 'int16')
print(a)

b= np.array([[2.3,4.5,3.4],[2.6,4.1,4.3]])
print(b)

#get dimensions
dimensions = a.ndim
print(dimensions)

#get shape
shape = b.shape 
print(shape)

#get type
print(a.dtype)
print(b.dtype)

#get size number of bytes
a.itemsize
b.itemsize

#get total size
a.size  + a.itemsize
a.nbytes

