
num = float(input("Enter a number: "))

    # Check if the number is Positive, Negative, or Zero [cite: 28-31]
if num > 0:
        print("The number is Positive.")
elif num < 0:
        print("The number is Negative.")
else:
        print("The number is Zero.")



# --- 2. Looping & Control Statements ---

print("Looping from 1 to 10:")

# Use a for loop from 1 to 10 [cite: 33]
for i in range(1, 11):
    
    # Use 'continue' to skip the number 3 [cite: 36]
    if i == 3:
        print(f"Skipping {i} (continue)")
        continue

    # Use 'pass' as a placeholder at number 5 [cite: 37]
    if i == 5:
        pass  # pass does nothing, just holds the structure
        print(f"Placeholder at {i} (pass executed)")

    # Use 'break' to stop the loop at number 8 [cite: 39]
    if i == 8:
        print(f"Stopping loop at {i} (break)")
        break

    # Display the current number
    print(f"Current Number: {i}")

else:
    # Loop else clause [cite: 7, 23]
    # This block executes only if the loop completes normally (without break).
    # Since we break at 8, this line will NOT print in this run.
    print("Loop finished successfully without breaking.")

print("\nProgram execution finished.")