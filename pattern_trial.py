# # SALES COMMISION PROGRAM


# keep_going = 'y'

# # Calculate a series of Commissions.

# while keep_going == 'y':
#     sales = float(input("Please Enter Sales Made: "))
#     comm_rate = float(input("Please Enter Commisions Rate: "))

#     commission = sales * comm_rate

#     print("The Commission is $", 
#           format(commission, ',.2f',), sep='')

    # keep_going = input("Do you want to Calculate another Commission again?"
    #                    "\nEnter y For Yes: ")
    
# print("\t\t\n Thank You, See You Agaain!")
# 5
# for name in ['Man', 'woman', 'humans']:
#     print(name)


# for items in ['Helena', 'Andre', 'Sam']:
#     print(items)
    

# print('Numbers \t\t Squares')
# print('---------------------------------')


# for number in range(1, 11):
#     square = number**2
#     print(number, '\t\t\t', square)


# AMANDA'S INHERITED CAR
# miles_per_hour_rate = 0.6214
# print("-----------------------")
# print('KPH', "\t", "\tMPH")
# print("-----------------------")
# for speed in range(50, 150, 10):
#     miles_per_hour = float(speed * 0.6214)

#     # Displaying the results
    
#     print(speed, '\t\t', format(miles_per_hour, '.1f'), sep='')    
# print("\n\tThank You!")

# LETTING THE USER CONTROL THE LOOP TYPE

# print("This Program displays numbers from 1 and their Squares \n")
# end = int(input("How far should i go? "))
# print("Numbers \t Squres")
# print('-----------------------')

# for number in range(1, end +1):
#     square = number ** 2
    
#     print(number, '\t\t', square)
    
# print("\n\tThank You !!!")


# A PROGRAM TO CALCULATE A RUNNING TOTAL

# accumulator = float(0.0)
# runner = 5

# for looper in range(runner):
    
#     sales = float(input(f"Please Enter For Day {looper + 1}" + " "))
#     accumulator += sales
    
# print("The Total Sales for the five"
#       " Days is $", format(accumulator, ',.2f'), sep='')

# SENTINEL PROGRAM

# print ("Please Enter Lot Number or 0 to exit")

# lot_counter = 0
# tax_factor = 0.0065

# lot = int(input("Please Enter Lot "))

# while lot != 0:
#     value = float(input("Enter the property value: "))
    
#     tax = value * tax_factor
    
#     print("Property Tax Is $", format(tax, ',.2f'), sep='')
    
#     print("Enter Lot Number Or 0 to Exit")
#     lot = int(input("Enter Lot Number: "))
    
# print("\t Thank You....")

# INPUT VALIDATION eg.1
# total = 0
# score = int(input("Please Enter Score: "))

# while score <= 0:
#     print("Error Please Enter a Significant Value")
#     score = int(input("Enter your Test score "))
    
# total += score

# print("your Score is ", total)
# print ("\t Thank You")

# mark_up = 2.5
# another = 'y'

# while another == 'y' or another == 'Y':
#     wholesale = float(input("Enter Wholesale Cost: "))
    
#     while wholesale < 0:
#         print("Error, please wholesale cannot be a negative value")
#         wholesale = float(input("Enter the Correct wholesale Cost: "))
    
#     retail = wholesale * mark_up
    
#     print("Retail Price is $", format(retail, ',.2f'), sep='')
    
#     another = input("Do you have another Item, Enter y for Yes. ")
    
# print('Thank You...')
    
    # NESTED LOOPS
    
# num_students = int(input("How Many Students do you have? "))

# number_of_Tests = int(input("How many Tests per students? "))

# for students in range(num_students):
#     total = 0.0
#     print("Students Number", students +1 )
#     print("----------------------")
#     for num_test in range(number_of_Tests):
#         print("Test Number", num_test + 1, end='')
#         score = float(input(": "))
#         total += score
         
#     average = total / number_of_Tests
        
#     print("The average for student number ", students + 1, " is: ", format(average, '.1f'), sep='')
#     print()
    


# # EXERCISE 15  TEST AVERAGE AND GRADE
# # (THIS PROGRAM WILL ALLOW THE USER TO
# # CALCULATE THE DESIRED NUMBER OF TESTS TAKEN), (USING THE FOR LOOP)


# def main():
#     accumulator = 0
#     test_taken = 5
#     mark1 = 100
#     mark2 = 100

#     for counter in range(test_taken):
#         test_score = input(f"Please enter your Score for test {counter + 1} : ")
#         convert = int(test_score)

#         accumulator += convert  # Accumulator for the average score
#         counter += 1  # counter to cut loop

#         #determine_grade(convert) # get grade 

#         print(mark2 - 10, "-", mark1, "\t", determine_grade(convert))
#         mark2 -= 10
#         mark1 -= 10 
#         mark1 -=1
        
#     get_average = calc_average(accumulator, test_taken)

#     # print("Score \t Letter Grade")
#     # print("_______________________")
#     # for check in range(test_taken):
#     #     print(mark2 - 10, "-", mark1, "\t", determine_grade(convert))
#     #     mark2 -= 10
#     #     mark1 -= 11
#     #     cut += 10
#     #     mark1 - cut

#     # Displaying the Average of score for the test taken
#     print("The Average Score is ", format(get_average, ',.2f'), sep='')


# def determine_grade(score):

#     if score > 89 <= 100:
#         grade = "A"

#     elif score > 79 and score >= 89:
#         grade = "B"

#     elif 69 > score <= 79:
#         grade = "C"

#     elif 59 > score <= 69:
#         grade = "D"
        
#     elif score < 60:
#         grade = "F"

#     return grade
        


# def calc_average(average, test_number):
#     average_score = float(average / test_number)
#     return average_score


# main()