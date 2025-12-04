def squ(a):
    square = a * a #or we can use pow(a,2)
    return square
n = int(input("Enter a number: "))
result = squ(n)
print("The square of", n, "is:", result)