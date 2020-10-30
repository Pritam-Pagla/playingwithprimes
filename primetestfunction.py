#just an utterly simple function to see whether a number is prime or not!

def primeTest(x):
    for divisor in range(2,x):
        if x%divisor == 0:
            # x is non prime
            return False
    return True
