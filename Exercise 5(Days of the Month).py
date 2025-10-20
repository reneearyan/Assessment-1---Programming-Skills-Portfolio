"""
Days of the Month with Bonus
"""
print("Days of the Month") #prints title
month_input=int(input("Enter the month number (1-12): ")) #asks the user to enter a month number

#dictionary of the days in each month
month_days= {1: "31 days", 2: "28 days", 3: "31 days",
        4: "30 days", 5:"31 days", 6: "30 days",
        7: "31 days", 8: "31 days", 9: "30 days", 
        10: "31 days", 11: "30 days", 12:"31 days"}

if 1 <= month_input<=12: #checks if the input is between 1 and 12
   if month_input==2: #for the month of February
     leap = input("Is it a leap year? (Yes or No): ") #asks user if it's a leap year
     if leap.lower()=="yes":
        print("There are 29 days in February.")
     else:
        print("There are 28 days in February.")
   else:
      print(f"There is {month_days[month_input]} in month {month_input}.") #prints from the dictionary
else:
    print("Invalid month number. Try again.") #if the number is not valid, user will try again.
