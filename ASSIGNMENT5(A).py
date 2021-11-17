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
import math
grade = math.ceil(gradePercentage)
if  grade>=96 and grade<=100:
    print(f"Grade/Mark: {gwaA}")
    print(F"Description: {DescriptionA}")
elif grade>=94 and grade<=96:
    print(f"Grade/Mark: {gwaB}")
    print(F"Description: {DescriptionA}")
elif grade>=91 and grade<=93:
    print(f"Grade/Mark: {gwaC}")
    print(F"Description: {DescriptionB}")
elif grade>=88 and grade<=90:
    print(f"Grade/Mark: {gwaD}")
    print(F"Description: {DescriptionB}")
elif grade>=85 and grade<=87:
    print(f"Grade/Mark: {gwaE}")
    print(F"Description: {DescriptionC}")
elif grade>=82 and grade<=84:
    print(f"Grade/Mark: {gwaF}")
    print(F"Description: {DescriptionC}")
elif grade>=79 and grade<=81:
    print(f"Grade/Mark: {gwaG}")
    print(F"Description: {DescriptionD}")
elif grade>=76 and grade<=78:
    print(f"Grade/Mark: {gwaH}")
    print(F"Description: {DescriptionD}")
elif 75<=grade:
    print(f"Grade/Mark: {gwaI}")
    print(F"Description: {DescriptionE}")
elif grade>=65:
    print(f"Grade/Mark: {gwaJ}")
    print(F"Description: {DescriptionF}")
else: 
    print("Invalid Input")
# Finally, run the entire peogram and know the value of your grade percenatage and the description.