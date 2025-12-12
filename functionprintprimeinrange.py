<<<<<<< HEAD
def prime(start, end):
    for num in range(start, end + 1):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                print(num)
startrange = int(input("Enter the start of the range: "))
endrange = int(input("Enter the end of the range: "))
prime(startrange, endrange)
=======
def prime(start, end):
    for num in range(start, end + 1):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                print(num)
startrange = int(input("Enter the start of the range: "))
endrange = int(input("Enter the end of the range: "))
prime(startrange, endrange)
>>>>>>> b15f203c3be1641aac48da3d44620d1a8b9f3cbc
