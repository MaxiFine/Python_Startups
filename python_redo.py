# top_side = 6

# for r in range(top_side):
#     for c in range(top_side - r):
#         print("&", end='')
#     print()    
    
    
# WORKING WITH MODULES

from json.tool import main
import math

# FUNCTION FOR AREA OF CIRCLE
def area(radius):
    return math.pi * radius**2


# FUNCTION FOR CIRCUMFERENCE
def circumference(radius):
    return 2 * math.pi * radius


# Area of a Rectangle 
def area(width, lenght):
    return width * lenght


# Perimeter of a Rectangle
def perimeter(width, lenght):
    return 2 * (width + lenght)
