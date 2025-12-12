a=input("Enter the word :")
if a==a[::-1]:
    print(f"The word {a} is palindrome.")
else:
    print(f"The word {a} is not palindrome.")