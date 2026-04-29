""" 
Challenge 1 : Self Intro script generator

Create a python script that interact with the user and generate personalized Self introduction

A program should be :
 1.Ask the user name,age,city,profession and the favourite hobby
 2.Form this data  warm friendly paragraph of self introduction
 3.Print the final paragraph in a clean and reable format.
 """

import datetime

name = input("What is your name? ")
age = int(input("What is your age? "))
city = input("What is your city ? ")
profession = input("What is your profession ? ")
hobby = input("What is your favourite hobby ? ")

input_data = (
    f"Hello , my name is {name} and am {age} years old. and live in {city}.\n I work as a {profession} and I absolute love my {hobby} in my free time."
)

current_date = datetime.date.today().isoformat()
input_data += f"\nLogged on : {current_date}"

border = "*" * 80
final_output = f"{border}\n{input_data}\n{border}"

print("\n")
print(final_output)





