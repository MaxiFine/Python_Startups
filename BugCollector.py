# BUDGET ANALYSIS EXERCISE
# USING THE WHILE LOOP

Accumulator = 00.0  # Accumulator For Expenses
cutter = 5  # iteration limit
totalBudget = float(input('\n\t Please Enter Your Budgeted Amount: '))

for mi in range(cutter):  # this loop is set to iterate 5 times
    expenses = float(input('\n\t Please Enter Expenses: '))
    Accumulator += expenses  # accumulator to take the Expenses from user
    cutter += 1  # iteration limit

AmtLeft = totalBudget - Accumulator
print('\t```````````````````````````')
print('\t Total Amount: ', format(AmtLeft, ',.2f'))
