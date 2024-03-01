def primes(n, print):
    primes_under_n = 0
    for i in range(2, n + 1):
        isPrime = True
        for j in range(2, i):
            if i % j == 0 :
                isPrime = False
                break
        if isPrime : 
            primes_under_n+=1
            if print : 
                print("{number} is a prime".format(number=i))
    return primes_under_n

n = 10_000
print("There are {number:_} primes under {n:_}".format(number=primes(n, False), n=n))
