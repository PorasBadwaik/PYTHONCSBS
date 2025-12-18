
num = float(input("Enter a number: "))
print("Use of if-elif-else")


    # Check if the number is Positive, Negative, or Zero [cite: 28-31]
if num== 0:
        print("The number is zero.")
elif num < 0:
        print("The number is Negative.")
elif num > 0:
        print("The number is positive.")
else :
        print("Enter the valid input.")



# --- 2. Looping & Control Statements ---

print("Use of for loop and control statements:")


# Use a for loop from 1 to 10 [cite: 33]
for i in range(1, 11):
    
    # Use 'continue' to skip the number 3 [cite: 36]
    if i == 3:
        print(f"Skipping {i} (continue)")
        continue

    # Use 'pass' as a placeholder at number 5 [cite: 37]
    if i == 5:
        pass  # pass does nothing, just holds the structure
        print(f"{i} (pass executed)(no operation)")

    # Use 'break' to stop the loop at number 8 [cite: 39]
    if i == 8:
        print(f" {i} (break encoumtered,looping stopped)")
        break
    else :
          print("For loop is finished")
    

n=1
while n<11:
    print(n,end=" ")
    n+=1