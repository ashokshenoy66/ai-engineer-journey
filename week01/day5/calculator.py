import math

def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    return a * b


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

def power(a:float, b:float)->float:
    ''' returns bth power of a '''
    return a**b

def modulus(a:float, b:float)-> float:
    ''' returns remainder of a/b i.e modulus '''
    return a % b

def square_root(num:float)->float:
    ''' returns square root of the input number '''
    return math.sqrt(num)

