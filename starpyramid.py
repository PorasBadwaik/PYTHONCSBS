<<<<<<< HEAD
row=int(input("Enter the no. of rows : "))
for n in range (row):
    print(" "*(row-n-1)+"*"*(2*n+1)) #full pyramid
for n in range (row+1):
    print("*"*(n))                   #right pyramid
for n in range (row):
=======
row=int(input("Enter the no. of rows : "))
for n in range (row):
    print(" "*(row-n-1)+"*"*(2*n+1)) #full pyramid
for n in range (row+1):
    print("*"*(n))                   #right pyramid
for n in range (row):
>>>>>>> b15f203c3be1641aac48da3d44620d1a8b9f3cbc
    print(" "*(row-n-1)+"*"*(n+1))   #left pyramid