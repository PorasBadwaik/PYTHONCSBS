def prime_in_range(a):
    primes = []
    for num in range(2, a + 1):
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes
n = int(input("Enter a number: "))

result = prime_in_range(n)
print(f"Prime numbers in the range 1 to {n} are: {result}")
