"""
 Challenge: Minutes Alive Calculator

Write a Python script that calculates approximately how many minutes old a person is, based on their age in years.

Your program should:
1. Ask the user for their age in years (accept float values too).
2. Convert that age into:
   - Total days
   - Total hours
   - Total minutes
3. Display the result in a readable format.

Assumptions:
- You can use 365.25 days/year to account for leap years.
- You don't need to handle time zones or exact birthdates in this version.

Example:
Input:
  Age: 25

Output:
  You are approximately:
    - 9,131 days old
    - 219,144 hours old
    - 13,148,640 minutes old

Bonus:
- Add comma formatting for large numbers
- Let the user try again without restarting the program
"""

def age_calculator(age):
    total_days = 365
    total_hours = 24
    total_minutes = 60

    total_aged_days = age * total_days
    total_aged_hours = total_aged_days * total_hours
    total_aged_minutes = total_aged_hours * total_minutes

    return round(total_aged_days) ,  round(total_aged_hours) , round(total_aged_minutes)

while True:
    try:
        age = float(input("enter your age! "))
        days , hours , minutes =  age_calculator(age)

        print("\n Your age is approximate : ")
        print(f" -  total days is {days} \n -  total hours is {hours} \n -  total minutes is {minutes}")

        again = input("would you like to try again?  (y/n)").strip().lower()

        if again != 'y':
            print("Good bye!")
            break


    except:
        print("your input is invalid")


