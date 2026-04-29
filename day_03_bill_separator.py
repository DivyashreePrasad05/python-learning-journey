"""
Challenge: Simple Bill Splitter

Write a Python script that helps split a bill evenly between friends.

Your program should:
1. Ask how many people are in the group.
2. Ask for each person's name.
3. Ask for the total bill amount.
4. Calculate each person's share of the bill.
5. Display how much each person owes in a clean, readable format.

Example:
Total bill: ₹1200  
People: Aman, Neha, Ravi

Each person owes: ₹400

Final output:
  Aman owes ₹400  
  Neha owes ₹400  
  Ravi owes ₹400

Bonus:
- Round to 2 decimal places
- Print a decorative summary box
"""

def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except:
            print("Invalid number")


num_input = int(input("How many peoples are in your group?  "))
names= []
 
for i in range(num_input):
    name = input(f"Enter the person# {i+1} : ").strip()
    names.append(name)

total_bill = get_float("Enter the amount in numbers only")

share = round(total_bill/num_input ,2)

print( "*" * 80)
print(f"Total amount : {total_bill} ")
print(f"Total split is : {share}")
print("final output:")

for name in names:
    print(f"{name} owes {share}")
    
print( "*" * 80)