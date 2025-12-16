def createandwrite(filename):
    with open(filename,"w") as f:
        f.write("This is the first line.\n")
        f.write("Python file handling is simple.\n")
    print("File created and written successfully.")
def read_file(filename):
    print("\n Reading the file contents:")
    with open(filename,"r") as f:
       print(f.read())
def append_file(filename, new_text):
    with open(filename,"a") as f:
        f.write(new_text +"\n")
    print("New line appended successfully.")
def search_file(filename):
    with open(filename,"r") as f:
        content =f.read()
        found=False
        if "Python" in content:
            print("Found it !!!!!!")
            found=True
        else:
            print("there is nothing like that..")
filename = "C:/Users/JSPM/Downloads/iris.csv"
createandwrite(filename)
read_file(filename)
append_file(filename,"Hey Buddy, how are you ?")
search_file(filename)