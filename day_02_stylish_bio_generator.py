"""
Challenge: Stylish Bio Generator for Instagram/Twitter

Create a Python utility that asks the user for a few key details and generates a short, stylish bio that could be used for social media profiles like Instagram or Twitter.

Your program should:
1. Prompt the user to enter their:
   - Name
   - Profession
   - One-liner passion or goal
   - Favorite emoji (optional)
   - Website or handle (optional)

2. Generate a stylish 2-3 line bio using the inputs. It should feel modern, concise, and catchy.

3. Add optional hashtags or emojis for flair.

Example:
Input:
  Name: Riya
  Profession: Designer
  Passion: Making things beautiful
  Emoji: 🎨
  Website: @riya.design

Output:
  🎨 Riya | Designer  
  💡 Making things beautiful  
  🔗 @riya.design

Bonus:
- Let the user pick from 2-3 different layout styles.
- Ask the user if they want to save the result into a `.txt` file.
"""


import textwrap
name = input(" Enter your name :").strip()
profession = input("Enter your profession :").strip()
passion = input("Enter your passion in one line :").strip()
emoji = input ("Enter a your favourite emoji : ").strip()
website = input("Enter your website : ").strip()

print("1.Simple bio ")
print(" 2.Vertical flair bio ")
print("3.Emoji Sandwitch bio ")

style = input("\n Select any option 1 , 2 , 3 \n").strip()

def generate_bio(style):
    if style == "1" :
        return f"{name}  | {passion} | {profession} | {website}"
    elif style == "2" :
        return f" {name} \n {passion} \n {profession} \n {website}"
    elif style == "3" :
        return f" {emoji * 3} \n {name} \n {passion} \n {profession} \n {website} \n {emoji * 3}"
    else :
        return "invalid choice"
       

bio = generate_bio(style)
print("\n Your  bio is generated \n")
print("*" * 50)
print(textwrap.dedent(bio)) 
print("*" * 50)

save = input("Do you want to save your bio into tet file ? y / n :").lower()

if save == "y":
    filename = f"{name .lower().replace(" " , "_")}_bio.txt"
    with open(filename , "w" , encoding="utf-8") as f:
        f.write(bio)
   
    print("file saved")