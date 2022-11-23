# WORKING WITH MODULES EXAMPLE ONE

import math

import circle       # Area of Circle
import rectangle    # Area of Rectangle

#  Constance for Menu
AREA_CIRCLE_CHOICE = 1
CIRCUMFERENCE_CHOICE = 2
AREA_RECTANGLE_CHOICE = 3
PERIMETER_RECTANGLE_CHOICE = 4
QUIT_CHOICE = 5

# THE MAIN FUNCTION

def main():
    choice = 0

    while choice != QUIT_CHOICE:
        display_menu()

        choice = int(input("Enter Your Choice: "))

        # Perform the Selected action
        if choice == AREA_CIRCLE_CHOICE:
            radius = float(input("Enter the circle's radius: "))
            print("The area is", format(circle.area(radius), ',.2f'))

        elif choice == CIRCUMFERENCE_CHOICE:
            radius = float(input("Enter Circle's Radius: "))
            print("The Circumference is", \
                format(circle.circumference(radius), ',.2f'))
        
        elif choice == AREA_RECTANGLE_CHOICE:
            width = float(input("Enter the rectangle's width: "))
            length = float(input("Enter the rectangle's lenght: "))
            print("The area is", format(rectangle.area(width, length), ',.2f'))

        elif choice == PERIMETER_RECTANGLE_CHOICE:
            width = float(input("Enter the rectangle's width: "))
            length = float(input("Enter rectangle's length: "))
            print("The Perimeter is", format(rectangle.perimeter(width, length)))

        elif choice == QUIT_CHOICE:
            print("Exiting the Program...")
            print("Bye...")

        else:
            print("Error: Invalid selection")
            

def display_menu():
    print("\t _Menu_")
    print("1) Area of a Circle")
    print("2) Circumference of a Circle")
    print("3) Area of Rectangle")
    print("4) Perimeter of a Rectangle")
    print("5) Quit")


main()



