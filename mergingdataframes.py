import pandas as pd
staff_df = pd.DataFrame([{'name':'kelly','role':'director'},
                        {'name':'sally','role':'course liason'},
                        {'name':'james','role':'grader'}])
staff_df = staff_df.set_index('name')
student_df = pd.DataFrame([{'name':'james','school':'business'},
                        {'name':'sally','school':'law'},
                        {'name':'mike','school':'engineering'}])
student_df = student_df.set_index('name')
print(staff_df.head())
print(student_df.head())

pd.merge(staff_df,student_df, how = 'outer', left_index = True, right_index = True)

# how attribute as inner
pd.merge(staff_df,student_df, how = 'inner', left_index = True, right_index = True)

pd.merge(staff_df,student_df, how = 'left', left_index = True, right_index = True)

pd.merge(staff_df,student_df, how = 'right', left_index = True, right_index = True)

staff_df = staff_df.reset_index()
student_df = student_df.reset_index()
pd.merge(staff_df,student_df, how = 'right', on = 'name')

staff_df = pd.DataFrame([{'name':'kelly','role':'director','location':'state street'},
                        {'name':'sally','role':'course liason','location':'washington avenue'},
                        {'name':'james','role':'grader','location':'washington avenue'}])
student_df = pd.DataFrame([{'name':'james','school':'business','location':'builliard avenue'},
                        {'name':'sally','school':'law','location':'fraternity house'},
                        {'name':'mike','school':'engineering','location':'wilson crescent'}])

pd.merge(staff_df,student_df, how = 'left', on = 'name')

staff_df = pd.DataFrame([{'name':'kelly','role':'director','last name':'dejardins'},
                        {'name':'sally','role':'course liason','last name':'brooks'},
                        {'name':'james','role':'grader','last name':'wild'}])
student_df = pd.DataFrame([{'name':'james','school':'business','last name':'hammond'},
                        {'name':'sally','school':'law','last name':'smith'},
                        {'name':'sally','school':'engineering','last name':'brooks'}])
pd.merge(staff_df,student_df, how = 'inner', on = ['name','last name'])