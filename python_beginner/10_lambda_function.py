# Example of lambda functions
# A lambda function is a small anonymous function that can take any number of arguments,
# but can only have one expression. It is often used for short, throwaway functions.

# Traditional function to double a number
def double(x):
    return x*2
print(double(3))

# Equivalent lambda function
double = lambda x: x*2
cube = lambda x: x**3
avg = lambda x, y: (x+y)/3

print(double(5))
print(cube(3))
print(avg(3,9))

# Using lambda function inside another function
def appl(func, value):
    return func(value)+6

print(appl(lambda x: x**3, 3))

# Using lambda function with map()
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print("Squared numbers using map and lambda: ", squared)

# Using lambda function with filter()
even_numbers = list(filter(lambda x: x%2==0, numbers))
print("Even numbers using filter and lambda: ", even_numbers)

# Using lambda function with sorted()
points = [(1, 2), (3, 1), (5, 4), (2, 3)]
sorted_points = sorted(points, key=lambda point: point[0]) # Sort by x-coordinate and set `point[1]` for y-coordinate
print("Points sorted by y-coordinate using sorted and lambda: ", sorted_points)

# Using lambda function with reduce()
from functools import reduce
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x*y, numbers)  # Calculates the product of all numbers in the list
print("Product of all numbers using reduce and lambda: ", product)

# Note: Lambda functions are best suited for simple operations. For more complex logic, it's better to use regular functions defined with def.

