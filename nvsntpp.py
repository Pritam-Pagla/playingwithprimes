no_of_skips=[0]      # skip_amount within which the ration of (Number of Twin Prime Paris vs Range; is to be determined)
twinPrime_dist=[]      # twinPrime_dist[1]={Number of Twin Prime Pairs within [0,(1*skip_amount)]}/{total numbe of natural numbers within the range}; it is the twinPrimeDistribution

print("\n")
print("Program for finding the twin-primes in a given range")
print("\n")

skip=int(input("Enter the skipping amount: "))
print("\n")

def primeTest(x):
    for divisor in range(2,x):
        if x%divisor == 0:   # x is non prime
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


lb = 2; # Lower bound of Natural Number for this calculation
ub = int(input("\nEnter the Upper Bound: "))


for skips in range(2, ub+1):              # for determining number of steps required correspnding the skip_amount and total range
    if skips%skip == 0:
        no_of_skips.append(skips)

nof=len(no_of_skips) # Number Of Skips(nof) in between

print(no_of_skips)


for nums in range(0,nof-1):
    ntpp_n_ratio = calculate_NTPP(no_of_skips[nums], no_of_skips[nums+1])/(skip)
    print(calculate_NTPP(no_of_skips[nums], no_of_skips[nums+1]))
    twinPrime_dist.append(ntpp_n_ratio)
    #print(ntpp_n_ratio)



print("\n")
print(twinPrime_dist)
print("\n\n")
