a=int(input("Enter your salary to calculate bonus:"))
if(a<=10000):
    print("Your bouns on salary is 10% so your bonus is:",(a*10)/100)
elif(20000>=a>10000):
    print("Your bonus on salary is 20% so your bonus is:",(a*20)/100)
elif(40000>=a>20000):
    print("Your bonus on salary is 30% so your bonus is:",(a*30)/100)
elif(60000>=a>40000):
    print("Your bonus on salary is 40% so your bonus is:",(a*40)/100)

