def temp(c):
    f = (c * 9/5) + 32
    return f
c = float(input("Enter temperature in Celsius: "))
result = temp(c)
print(f"The temperature in Fahrenheit is: {result}°F")