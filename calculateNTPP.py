def primeTest(x):
    for divisor in range(2,x):
        if x%divisor == 0:
            # x is non prime
            return False
    return True

def calculate_NTPP(y,z):    # y=lower-bound & z=upper bound
    primes_within=[]
    for integer in range(y,z):
        if(primeTest(integer)==True and primeTest(integer+2)==True):
            primes_within.append(str(integer)+','+str(integer+2))

    ntpp = len(primes_within)  # ntpp = Number of Twin Prime Pairs
    return ntpp
    primes_within=[]

def determine_pairs(y,z):    # y=lower-bound & z=upper bound
    primes_within=[]
    for integer in range(y,z):
        if(primeTest(integer)==True and primeTest(integer+2)==True):
            primes_within.append(str(integer)+','+str(integer+2))

    return primes_within
    primes_within=[]

print("\n")
lb = 2
ub = int(input("Enter the upper bound: "))

print("\n")
print(calculate_NTPP(lb,ub))
print("\n")
print(determine_pairs(lb,ub))
