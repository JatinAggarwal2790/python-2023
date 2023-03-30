# default args
def add(a,b=10):
    return a+b

print(add(3,4))
print(add(3))

# keyword args

def wish(name, age):
    print(f"Hello {name} you are {age} years old")


wish("India", 75)
# calling a function using keyword arguments
wish(age=75, name="India")

# mutiple returns
def sum_diff(a,b):
    return a+b, a-b

x,y = sum_diff(6,2)
print(x,y)

# docstrings
def add(a,b):
    """ this function adds two
    numbers and returns their sum"""
    return a+b

help(add)

# variable length args
# variable length keyword args

