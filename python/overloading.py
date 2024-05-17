#using dispatch

from multipledispatch import dispatch

@dispatch(int, int)
def product(first, second):
    result = first*second
    print(result)

@dispatch(int, int, int)
def product(first, second, third):
    result = first * second * third
    print(result)

product(2, 5)
product(2, 5, 2)

