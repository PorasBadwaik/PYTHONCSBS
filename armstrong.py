a=int(input("Enter the number: "))      #ARMSTRONG NUMBER : THE NUMBER WHOSE SUM OF CUBE INDIVISUAL DIGIT IS EQUAL TO ITSELF
temp=a                                  #EX 153=1^3+5^3+3^3
sum=0
digits=len(str(a))

while temp>0:
    digit=temp%10
    sum +=digit**digits
    temp //=10

if sum==a:
    print(f"The given number {a} is an Armstrong number.")
else:
    print(f"The given number {a} is not an Armstrong number.")