x = 1
y = 2
x + y

def add_numbers(x,y):
    return x + y

add_numbers(1,2)

def add_numbers(x, y, z=None):
    if(z == None):
        return x + y
    else:
        return x + y + z

print(add_numbers(1,2))

print(add_numbers(1,2,3))
        
def add_numbers(x, y, z=None, flag=False):
    if(flag):
        print("flag is true")
    if(z==None):
        return x+y
    else:
        return x+y+z
    
print(add_numbers(1,2,flag=True))
        
        