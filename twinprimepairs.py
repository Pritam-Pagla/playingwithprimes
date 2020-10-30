# finding the twin prime pairs

twin_primes=[]
print("\n")
print("Program for finding the twin-primes in a given range")
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
    if(primeTest(integer)==True and primeTest(integer+2)==True):
        twin_primes.append(str(integer)+','+str(integer+2))

print("\n")
print("Number of Primes: "+str(len(twin_primes)))
print("\n")
print(twin_primes)
print("\n\n")

