global_v=10
def add(a,b):
    return a+b
def scope():
    local =5
    print("Local variable:",local)
    print("Global variable:",global_v)
result=add(3,4)
print("Sum:",result)
scope()
print("Global variable outside function:",global_v)
    