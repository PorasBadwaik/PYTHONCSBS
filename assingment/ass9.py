def create():
    with open("intel.txt", "w") as f:
        f.write("Hi I am Poras!!\n")
        print("Created amd written")
def read_file():
    with open("intel.txt", "r") as f:
        print(f.read())
def append_file():
    with open("intel.txt", "a") as f:
        f.write("This is appended line!!\n")
def search_file():
    with open("intel.txt", "r") as f:
        content = f.read()
        if "Poras" in content:
            print("Exists!!")
        else:
            print("Not Exists!!")
create()
append_file()
read_file()
search_file()