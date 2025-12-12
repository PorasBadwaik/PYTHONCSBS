<<<<<<< HEAD
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact
n = int(input("Enter a number to find its factorial: "))

=======
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact
n = int(input("Enter a number to find its factorial: "))

>>>>>>> b15f203c3be1641aac48da3d44620d1a8b9f3cbc
print("The factorial of", n, "is:", factorial(n))