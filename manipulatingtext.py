import re

# match(), search()
text = 'this is a good day'
if(re.search("good",text)):
    print("wonderful")
else:
    print("alas! ;(")

#tokenizing, findall(), split()
text = 'amy works diligently. amy gets good grades. our student amy is successful'
re.split("amy",text)

re.findall("amy",text)

text = 'amy works diligently. amy gets good grades. our student amy is successful'
re.search("^amy",text)

#patterns and character classes
grades = "AAABCDAABDDAAA"
re.findall("B",grades)

re.findall("[AB]",grades) #set operator