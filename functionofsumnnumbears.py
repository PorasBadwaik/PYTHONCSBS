def sum(a):
    total = 0
    for i in range(1, a + 1):
        total += i
    return total
n = int(input("Enter a number: "))
result = sum(n)
print("The sum of first", n, "natural numbers is:", result)