import numpy as np
import math

a = np.array([1,2,3])
print(a)
print(a.ndim)
b = np.array([[1,2,3],[4,5,6]])
print(b)
print(b.ndim)
b.shape
# we can also check the type of items in the array
a.dtype
#besides integers floats are also accepted in numpy arrays
c = np.array([2.2,3,4.4])
print(c)
print(c.ndim)
c.dtype.name

#lets look at the data in out array
c

d = np.zeros((2,3))
print(d)

e = np.ones((2,3))
print(e)

#we can also generate arrays with random numbers
np.random.rand(2,3)

# we can create a sequence of numbers using arange() function. the first argument is the starting bound, the second argument
# is the ending bound and the thirs argument is the difference between each consecutive numbers

f = np.arange(10,50,2)
print(f)

# if we want to generate a sequence of floats use linspace(). the third argument is the total number of items u want to generate
g = np.linspace(0, 2, 15)
print(g)

# arithmetic operators on arrays apply elementwise
a = np.array([10,20,30,40])
b = np.array([1,2,3,4])
c = a-b
print(c)
d = a*b
print(d)

#with arithmetic manipulation we can convert data to the way we want it to be
farenheit = np.array([1, -10, -15, -5, 0])
celcius = (farenheit-31) * (5/9)
celcius

#boolean
celcius > -20

#modulus
celcius % 2 == 0

#matrix manipulation
a = np.array([[1,1],[0,1]])
b = np.array([[2,1],[2,0]])
print(a*b)
print(a@b)

a = np.array([1,2,3,4])
b = np.array([1.1,2.2,3.3,4.4])
c = a + b
print(c)

print(c.sum())
print(c.max())
print(c.min())
print(c.mean())


b = np.arange(1,16,1).reshape(3,5)
print(b)

from PIL import Image
from IPython.display import display
im = Image.open('ironman.tiff')
display(im)
array = np.array(im)
print(array.shape)
array

mask = np.full(array.shape,255)
mask

modified_array = array - mask
modified_array = modified_array * -1


#indexing
a = np.array([1,3,5,7])
a[2]
a = np.array([[1,2],[3,4],[5,6]])
a

#slicing
a = np.array([0,1,2,3,4,5])
print(a[:3])