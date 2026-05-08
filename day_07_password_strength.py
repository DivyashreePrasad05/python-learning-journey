"""
 Challenge: Password Strength Checker & Suggestion Tool

Build a Python script that checks the strength of a password based on:
1. Length (at least 8 characters)
2. At least one uppercase letter
3. At least one lowercase letter
4. At least one digit
5. At least one special character (e.g., @, #, $, etc.)

Your program should:
- Ask the user to input a password.
- Tell them what's missing if it's weak.
- If the password is strong, confirm it.
- Suggest a strong random password if the input is weak.

Bonus:
- Hide password input using `getpass` (no echo on screen).
"""

import string
import random
import getpass

def password_strength_checker(password):
    issues = []

    if len(password)<8:
        print("Too short add minimum 8 characters")

    if not any(c.islower() for c in password):
        issues.append("Your password is missing lower latter")
    if not any(c.isupper() for c in password):
        issues.append("Your password is missing upper latter")
    if not any(c.isdigit() for c in password):
        issues.append("Your password is missing digit")
    if not any( c in string.punctuation for c in password):
        issues.append("Your password is missing special characters(eg:@,#,$,&,*)")
    return issues

def password_suggestion(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(chars) for _ in range(length))


password = getpass.getpass("Enter a password  : ")
issues = password_strength_checker(password)

if not issues:
     print("Strong password! ")
else:
    print("Weak password!")
    for issue in issues:
        print(f"-{issue}")

suggestion = password_suggestion()
print("\n suggesting you a strong password")
print(suggestion)


