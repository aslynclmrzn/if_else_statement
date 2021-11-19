# Program 2: Find the lowest number
# Create a program that will ask for three numbers.
inputA = int(input('Enter 1st number: '))
inputB = int(input('Enter 2nd number: '))
inputC = int(input('Enter 3rd number: '))
# Conditional statements for lowest number.
if (inputA < inputB) and (inputA < inputC):
    lowestValue = inputA
elif (inputB < inputA) and (inputB < inputC):
    lowestValue = inputB
else:
    lowestValue = inputC
# Display the lowest number among the three numbers.
print(f"The lowest number among {inputA}, {inputB}, and {inputC} is: {lowestValue}")