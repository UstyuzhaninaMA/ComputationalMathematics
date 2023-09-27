import math

def formula1(x, h, fn):
    return (fn(x + h) - fn(x)) / h

def formula2(x, h, fn):
    return (fn(x) - fn(x - h)) / h

def formula3(x, h, fn):
    return (fn(x + h) - fn(x - h)) / (2 * h)

def formula4(x, h, fn):
    return (4 * (fn(x + h) - fn(x - h)) / ( 3 * 2 * h) - 
            (fn(x + 2 * h) - fn(x - 2 * h)) / ( 3 * 4 * h))

def formula5(x, h, fn):
    return (3 * (fn(x + h) - fn(x - h)) / ( 2 * 2 * h) - 
            3 * (fn(x + 2 * h) - fn(x - 2 * h)) / ( 5 * 4 * h) + 
            (fn(x + 3 * h) - fn(x - 3 * h)) / ( 10 * 6 * h))