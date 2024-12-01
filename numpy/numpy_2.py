# Initialising different types of arrays
import numpy as np

a = np.array([[1, 2, 3],[4, 5, 6]])
# all zeroes matrix
print(np.zeros((2,3)))

#all ones
print(np.ones((2,3)))

#any other numbers
#np.full((r,c),value)
print(np.full((2, 3), 7))

#take refrence from exsisting array
print(np.full_like(a,4))

#print random array
print(np.random.rand(2,3))

#random int array
print(np.random.randint(0,7,(2,3)))

#identity matrix
print(np.identity(2))

#repeating an array
b = np.array([[1,2,3]])
c = np.repeat(b , 2, axis=0)
print(c)

#Exercise 1

#Practise
a = np.ones((5,5),dtype=int)
c=np.zeros((3,3))
c[1,1] = 9
print(c)

#Inserting an array into another array
#a[row:row, column:column]= some array
a[1:4, 1:4]=c
print(a)

#copying Array
b=a.copy()
