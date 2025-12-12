a=[1,2,3,4,5,6,7,8,9,10]
def even(a):
    count=0
    for i in a:
        if i%2==0:
            count+=1
    return count
result=even(a)
print("The count of even numbers in the list is:",result)