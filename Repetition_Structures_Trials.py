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
#     print("-------------------")
#     for num_test in range(number_of_Tests):
#         print("Test Number", num_test + 1, end='')
#         score = float(input(": "))
#         total += score
         
#     average = total / number_of_Tests
        
#     print("The average for student number ", 
#           students + 1, " is: ", format(average, '.1f'), sep='')
#     print()

# for c in range(8):
#     for r in range(6):
#         print("*", end='')
#     print()
   
   # ASCENDING ORDER
# for c in range(8):
#     for r in range(c + 1):
#         print("#", end='')
#     print()
    
    # DECENDING ORDER
# for c in range(8, 0,-1):
#     for r in range(c):
#         print("$", end='')
#     print()

# Bug COLLECTOR *For Loop trial

# accumulator = 0.0   # ACCUMULATOR
# days = 5            # DAYS CHECKER

# for day_checker in range(days):
#     bugs = float(input(f"Enter Bugs Collected for Day {day_checker + 1}" + " "))
#     day_checker += 1
    
#     accumulator += bugs
    
# print("The Total Bugs Collected withhin " 
#       + str(day_checker), "days is", format(accumulator, ',.2f')) 

# print("\t Thank You...")

# USING THE WHILE LOOP TRIAL FOR BUGS COLLELCTIONS 

# accumulate = 0.0
# looper = 0

# while looper != 5:
#     bugs = float(input(f"Please Enter Bugs Collected for Day {looper + 1} "))
#     accumulate += bugs
#     looper +=1
    
# print(f"The Total Bugs Collected in {looper} Days is ", 
#       format(accumulate, ',.2f'))


# BUDGET ANALYSIS using the for loop

# total_amount = float(input("Please Enter the Amount here: "))
# accumalator = 0.0

# for looping in range(5):
#     expenses = float(input(f"Please Enter Expense {looping + 1} "))
#     looping += 1
    
#     accumalator += expenses
    
# if accumalator < total_amount:
#     excess = total_amount - accumalator
#     print("Great You're within Budget, Amount Left is $", format(excess, ',.2f'), sep='')
# elif accumalator > total_amount:
#     excess = total_amount - accumalator
#     print("You're out of Budget, Exceeded by $", format(excess, ',.2f'), sep='')


# EXERCISE 4 DISTANCE TRAVELLED

# speed = float(input("Please Enter Speed: "))
# time = int(input("Please Enter Time Traveled: "))

# print("Hour \tDistance Traveled")
# print("--------------------------")

# for check in range(time):
#     looper = check + 1
#     distance = speed * looper
#     print(looper, "\t", distance)
    
# # AVERAGE RAINFALL EXERCISE

# accumulator = 0.0
# months = 12
# years = int(input("Please Enter Years: "))
# checker = 0
# for rain in range(years):
#     for rain in range(months):
#        rainfall = float(input(f"Please Enter Rainfall month {rain + 1}: "))
#        accumulator += rainfall

# average = rainfall / years
# print("The Average Rainfall is", average, "Total Rainfall", accumulator, "for", months, "months")


# # CELSUIS TO FARENHEIT TABLE

# print("Celsius \t Fahrenheit")
# print("----------------------------")

# for looper in range(0, 21):
#     fah = 1.8 * looper + 32
#     looper + 1
#     print(looper, "\t\t", format(fah, '.1f'))

# # Penny Per Day

# days = int(input("Please Enter Number of Days: "))

# print("Days", "\t", "Salary")
# print("------------------------")
# salary = 0.0

# for checker in range(days):
#     checker + 1
#     total_pay = checker + 1
#     salary += total_pay
#     print(checker +1, "\t", total_pay)
    

# print("\n The total Salary is $", format(salary, ',.2f'), sep='')
# print("\t Thank You...")
    
    
# # Sum of Numbers 

# accumulator = 0.0

# nums = int(input("Please Enter Number: "))

# while nums > 0:
#     accumulator += nums
#     nums = int(input("Please Enter Number or Negative Integer to end Series: "))
    
    
# print("The sum of all the numbers is", accumulator)
    
# # OCEAN LEVELS

# rising_level = 1.6
# years = 25
# check = 0
# accum  = 0
# print("Years ", "\t ", "Rising Levels")
# print("-------------------------")

# for check in range (years):
#     new_var = check + 1
    
#     rising = rising_level * new_var
#     accum += rising
#     print(check + 1 , "\t", format(rising, ',.2f'))
    
    
# print("The Total Rising Level is", format(accum, '.2f'), f"in {years} years" )

# tuition = 8000
# years = 5
# Accumulator = 0.0
# total_add = 0.0

# print("Years", "\t", "Tuition")
# print("------------------------")

# for checker in range(years):
#     checker + 1
#     increment = 0.03 * tuition
#     total_add += increment
    
#     Accumulator = tuition + total_add 
    
#     print(checker +1, "\t ", format(Accumulator, ',.2f'))
# print("\t Thank You...")


# FACTORIAL TRIAL Number EXs 111

number = int(input("Please Enter Number: "))
checker = 1

for looper in range(checker, number + 1):
    checker *= looper 
   
print("The Factorial of the number is:", checker)
    
