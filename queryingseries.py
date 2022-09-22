# a pandas series can be queried either by the index position or the index label. to query by numeric location starting with
# zero use iloc attribute. To query by index label you can use loc attribute. 
import pandas as pd
student_classes = {'alice':'physics',
                  'jack':'chemistry',
                  'molly':'english',
                  'sam':'history'}
s = pd.Series(student_classes)
s

s.iloc[3]
s.loc['molly']
# pandas tries to make our code a bit more readable and provides a smart syntax using the indexing operator directly on the 
# series itself
s[3]
class_code = {99 : 'english',
             100 : 'physics',
             101 : 'chemistry',
             102 : 'history'}
s = pd.Series(class_code)
#iterate over all the items in the series and invoke the required operation.
grades = pd.Series([90,80,70,60])
total = 0
for grade in grades:
    total += grade
print(total/len(grades))
#supports a method of computation called vectorization 
import numpy as np
total = np.sum(grades)
print(total/len(grades))

numbers = pd.Series(np.random.randint(0,1000,10000))
numbers.head()

#the ipython interpreter has something called magic function that begins with a percentage sign. 
# we are going to write a cellular magic function. 
%%timeit -n 100
total = 0
for number in numbers:
    total += number
total/len(numbers)

%%timeit -n 100
total = np.sum(numbers)
total/len(numbers)

for label,value in numbers.iteritems():
    numbers.set_value(label, value+2)
numbers.head()
    

%%timeit -n 10
s = pd.Series(np.random.randint(0,1000,10000))
for label,value in s.iteritems():
    s.loc[label]=value*2
    
%%timeit -n 10
s = pd.Series(np.random.randint(0,1000,10000))
s+=2

s = pd.Series([1,2,3])
s.loc['history'] = 102
s

student_classes = pd.Series({'alice':'physics',
                  'jack':'chemistry',
                  'molly':'english',
                  'sam':'history'})
student_classes

kelly_classes = pd.Series(['philosphy','arts','math'], index = ['kelly','kelly','kelly'])
kelly_classes

