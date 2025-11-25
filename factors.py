#-------------------
# is f a factor of n
#-------------------

def checkFactors(n, f):
    if n % f == 0:
        return True
    else:
        return False
    
#-------------------
# list of factors
#-------------------

def listFactors(n):
    factors = []
    for i in range(1, n + 1):
        if checkFactors(n, i):
            factors.append(i)
    return factors

#-------------------
# if a number is prime
#-------------------

def isPrime(n):
    if listFactors(n) == [1, n] or n == 1:
        return True
    else:
        return False
    
#-------------------
# list of all primes up to n
#-------------------
def allPrimes(n):
    primes = []
    for i in range(1, n + 1):
        if isPrime(i):
            primes.append(i)
    return primes

#-------------------
# product of prime factors
#-------------------      
def productOfPrimes(n):
    factors = listFactors(n)
    primes = []
    for i in factors:
        if isPrime(i):
            primes.append(i)
    product = n
    primeFactors = []
    while product != 1:
        for i in allPrimes(n):
            if checkFactors(product, i):
                product = product // i
                if i != 1:
                    primeFactors.append(i)
            else:
                continue
    primeFactors.append(1)
    primeFactors.sort()
    return primeFactors

# -------------------
# highest common factor
# -------------------

def hcf(n, f):
    commonFactors = []
    nFactors = listFactors(n)
    fFactors = listFactors(f)
    for i in nFactors:
        for j in fFactors:
            if i == j:
                commonFactors.append(i)
    return max(commonFactors)
 
print(hcf(74, 148))
    
    
                                    
