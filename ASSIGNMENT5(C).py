# Create a program that ask for an age of a person
# Display the life stage of the person.
from datetime import date
# This will ask for your birth year, month, and day.
Year = (int(input("Enter your Birth Year: ")))
Month = (int(input("Enter your Birth Month(eg.June = 06): ")))
Day = (int(input("Enter your day of Birth: ")))
# This code will compute your input birthmonth to your current age
today = date.today()
age = today.year - Year - ((today.month, today.day) < (Month, Day))
# This will display your age based on your input birthmonth
print (f"You are {age} years old.")

# Conditional statements for life stages
if (age<=0) and (age<=12):
    print (f'{age} : Kid')
elif (age>=13) and (age<=17):
    print (f'{age} : Teen')
elif (age==18):
    print (f'{age} : Debut')
else:
    print (f'{age} : Adult')
#Rules:
#0 - 12 : Kid
#13 - 17 : Teen
#18 : Debut
#19 above : Adult