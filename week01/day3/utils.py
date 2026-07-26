''' Functions to find out if a number is even , prime and to take factorial'''

def is_even(number:int)->bool:
    """
    Checks if the number is even
    """
    return number % 2 == 0
    

def is_prime(number: int) -> bool:
    """
    Checks to see if number is prime.
    """
    if number < 2:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True
        
    

def factorial(number:int)->int:
    """
    finds factorial of the number input.
    """
    fac = 1
    if number < 0:
        raise ValueError("Factorial is not defined for negative numbers.")

    for i in range(1, number + 1):
        fac = fac * i
    return fac

