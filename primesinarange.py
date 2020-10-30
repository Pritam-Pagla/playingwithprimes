primes=[]
print("\n")
print("Program for finding all primes within a range")
print("\n")

def primeTest(x):

    for divisor in range(2,x):
        if x%divisor == 0:
            # x is non prime
            return False
    return True

lb = int(input("Enter the lower-bound: "))
ub = int(input("Enter the upper-bound: "))

for integer in range(lb, ub):
    if(primeTest(integer)==True):
        primes.append(integer)

print("\n")
print("Number of Primes: "+str(len(primes)))
print("\n")
print(primes)
print("\n\n")

