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


#Initializing different types of arrays
#All 0s matrix

np.zeros(5)
np.zeros(2,3)
np.zeros(2,3,3,2)

#all 1s matrix
np.ones((4,2,2) ,dtype='int32')

#any number it has 2 parameters :shape , value
np.full((2,2),99, dtype='float32')

#any other full like
np.full_like(a, 4)

#or the same would be
np.full(a.shape, 4)

#random decimal numbers between 0 and 1
np.random.rand(4,2)
np.random.rand(4,2,3)
np.random.rand(4,2,3)

np.random_sample(a.shape)

#random integer values
np.random.randint(7)
np.random.randint(7, size = (3,3))
np.random.randint(4,7, size = (3,3))

#identity
np.identity(3)

#repeat array
arr = np.array([1,2,3])
r1 = np.repeat(arr, 3)
print(r1)

arr = np.array([[1,2,3]])
r1 = np.repeat(arr, 3, axis = 0)
print(r1)

#small problem
output = np.ones((5,5))
z =np.zeros((3,3))
z[1,1] = 9

output[1:4,1:4] = z
output[1:-1,1:-1] = z










