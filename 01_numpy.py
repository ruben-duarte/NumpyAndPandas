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

#accessing / changing specific elements .... rows, columns

a = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print(a)

#get specific elements [row, column] count from 0

#get 12
a[1,4]
a[1,-3]  #is the same

#get an specific row
a[0, :]
#get an specific column
a[: , 2]
#more fancy [startindex:endindex:stepsize]
a[0, 1:6:2 ]
a[0, 1:-1:2 ]

#changevalue
a[1,5] = 20

a[: , 2] = 5
a[: , 2] = [1,2]

#3d example

b = np.array([[[],[]],[[],[]]])
b = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(b)
b[0,1,1]
b[:,1,:]
#replace
b[ : , 1, :] = [[9,9],[8,8]]










