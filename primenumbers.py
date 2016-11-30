#the function that generates the primenumbers for numbers in a given range
def prime_numbers(n):
    primes = []
    for x in range(2 , n+1):
        for i in range(2 , x+1):
            if x % i == 0:
                break
        else:
            primes.append(x)
    return primes
