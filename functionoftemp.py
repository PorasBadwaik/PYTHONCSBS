def temp():
    c = int(input("Enter temperature in Celsius: "))
    f = (c * 9/5) + 32
    return f
print("Temperature in Fahrenheit:", temp())