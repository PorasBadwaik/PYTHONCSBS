def area(r):
    area = 3.14 * r * r
    return area
radius = float(input("Enter the radius of the circle: "))
print("The area of the circle with radius", radius, "is:", area(radius))