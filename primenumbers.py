#the function that generates the primenumbers for numbers in a given range
def prime_numbers(n):
    primes = []
    if  n < 0:
        return("You cannot enter negative numbers")
    else:
        for x in range(2 , n+1):
            for i in range(2 , x):
                if x % i == 0:
                    break
            else:
                primes.append(x)
        return primes

print(prime_numbers(10))
