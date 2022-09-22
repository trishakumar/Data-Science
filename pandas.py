import pandas as pd
students = ['alice', 'jack', 'molly']
pd.Series(students)

numbers = [1,2,3]
pd.Series(numbers)
# in python we have none type that indicates the lack of data
# underneath pandas does some type conversion for us. If we create a list of strings and we have one element, the none type, 
# pandas inserts it as a None and uses the type object for the underlying array
students = ['alice', 'jack', None]
pd.Series(students)

numbers = [1,2,None]
pd.Series(numbers)

# NaN is not equivalent to None. 
import numpy as np
np.nan == None

np.nan == np.anan
# we need to use special functions to test the presence of not a number such as numpy library isnan()
np.isnan(np.nan)

student_scores = {'alice':'physics',
                  'jack' : 'chemistry',
                   'molly': 'english'}
s = pd.Series(student_scores)
s

students = [("alice","brown"),("molly","green"),("jack","black")]
pd.Series(students)

s = pd.Series(['phyics','chemistry','english'],index = ['alice','jack','molly'])
s

student_scores = {'alice':'physics',
                  'jack' : 'chemistry',
                   'molly': 'english'}
s = pd.Series(student_scores, index = ['alice','molly','sam'])
s