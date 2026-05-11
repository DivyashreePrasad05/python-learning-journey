"""
 Challenge: Friendship Compatibility Calculator

Build a Python script that calculates a fun "compatibility score" between two friends based on their names.

Your program should:
1. Ask for two names (friend A and friend B).
2. Count shared letters, vowels, and character positions to create a compatibility score (0-100).
3. Display the percentage with a themed message like:
   "You're like chai and samosa — made for each other!" or 
   "Well... opposites attract, maybe?"

Bonus:
- Use emojis in the result
- Give playful advice based on the score range
"""

def friendship(name1 , name2):
    score = 0
    name1 , name2 = name1.lower(), name2.lower()
    common_letter = set(name1) & set(name2)
    vowels = set("aeiou")
    score += len(common_letter) * 5
    score += len(common_letter & vowels) * 10

    return min(score , 100)


def run_friendship_calculator():
    print("❤️ Friendship Compatibility calculator ❤️")
    name1 = input("Enter name1")
    name2 = input("Enter name2")

    calculator =friendship(name1 , name2)
    print(f"\n Score of your friendship : {calculator} ")
    
    if calculator >80:
        print("Your are prefect together like chai and biscute")
    elif calculator >= 30:
        print("You both look nice together make it better and best!")
    else:
        print("your coffee and tea dont match together!")


run_friendship_calculator()
