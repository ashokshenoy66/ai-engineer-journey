def is_even(number:int)->bool:
    return number % 2 == 0
    

def is_prime(number:int)->bool:
    if number < 2:
        return False
    else:
        num_prime = True

        for i in range(2, number):
            if number % i == 0:
                num_prime = False
                break

        if num_prime:
            return True
        else:
            return False
        
    

def factorial(number)->int:
    fac = 1

    for i in range(1, number + 1):
        fac = fac * i
    return fac

