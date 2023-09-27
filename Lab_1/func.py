import math

def function1(x):
    return math.sin(x * x)

def der_of_func1(x):
    return 2 * x * math.cos(x * x)

def function2(x):
    return math.cos(math.sin(x))

def der_of_func2(x):
    return -math.cos(x) * math.sin(math.sin(x))

def function3(x):
    return math.exp(math.sin(math.cos(x)))

def der_of_func3(x):
    return function3(x) * (- math.sin(x) * math.cos(math.cos(x)))

def function4(x):
    return math.log(x + 3)

def der_of_func4(x):
    return 1 / (x + 3)

def function5(x):
    return (x + 3) ** 0.5

def der_of_func5(x):
    return 1 / (2 * function5(x))
