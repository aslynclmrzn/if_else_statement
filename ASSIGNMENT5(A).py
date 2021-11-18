# Task: Create a program that will ask for grade percentage. Display the equivalent Grade/Mark and Description.
# create a program that let the user input their grade percentage. 
gradePercentage = float ((input('Enter your grade percentage: ')))
# Define gwaEquivalent() then use return command to return the multiple values in the function.
def gwaEquivalent():
    A = 1.0
    B = 1.25
    C = 1.5
    D = 1.75
    E = 2.0
    F = 2.25
    G = 2.5
    H = 2.75
    I = 3.0
    J = 5.0
    return A, B, C, D, E, F, G, H, I, J
# Define gradeDescription() then use return command to return the multiple values in the function.
def gwaDescription():
   categoryA = "Excellent"
   categoryB = "Very Good"
   categoryC = "Good"
   categoryD = "Satisfactory"
   categoryE = "Passing"
   categoryF = "Failure"
   return categoryA, categoryB, categoryC, categoryD, categoryE, categoryF
# Call the function for:
gwaA, gwaB, gwaC, gwaD, gwaE, gwaF, gwaG, gwaH, gwaI, gwaJ = gwaEquivalent()
DescriptionA, DescriptionB, DescriptionC, DescriptionD, DescriptionE, DescriptionF = gwaDescription()
# Then create a program that display the equivalent Grade/Mark and Description as an output.
# Conditional statement in rounding off grade percentage
import math
if float (gradePercentage%2>=0.5):
    grade = math.ceil(gradePercentage)
elif float (gradePercentage%2<=0.5):
    grade = round(gradePercentage)
# Conditional statement for the grade equivalent and description of grade percentage.
if grade>=97 and grade<=100:
    print(f"Grade/Mark: {gwaA}")
    print(F"Description: {DescriptionA}")
elif 96>=grade>=94:
    print(f"Grade/Mark: {gwaB}")
    print(F"Description: {DescriptionA}")
elif 93>=grade>=91:
    print(f"Grade/Mark: {gwaC}")
    print(F"Description: {DescriptionB}")
elif 90>=grade>=88:
    print(f"Grade/Mark: {gwaD}")
    print(F"Description: {DescriptionB}")
elif 87>=grade>=85:
    print(f"Grade/Mark: {gwaE}")
    print(F"Description: {DescriptionC}")
elif 84>=grade>=82:
    print(f"Grade/Mark: {gwaF}")
    print(F"Description: {DescriptionC}")
elif 81>=grade>=79:
    print(f"Grade/Mark: {gwaG}")
    print(F"Description: {DescriptionD}")
elif 78>=grade>=76:
    print(f"Grade/Mark: {gwaH}")
    print(F"Description: {DescriptionD}")
elif 75<=grade==75:
    print(f"Grade/Mark: {gwaI}")
    print(F"Description: {DescriptionE}")
elif 74>=grade>=65:
    print(f"Grade/Mark: {gwaJ}")
    print(F"Description: {DescriptionF}")
else: 
    print("Invalid Input")
# Finally, run the entire program and know the value of your grade percentage and the description.