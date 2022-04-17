# Get input from the user
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

# Concatenate the 2 names and make the letters all in lower case
name = name1 + name2
name_lower = name.lower()

# Find the numbers of letters in 'true' and 'love' in the concatenated name
true = name_lower.count("t")+name_lower.count("r")+name_lower.count("u")+name_lower.count("e")
love = name_lower.count("l")+name_lower.count("o")+name_lower.count("v")+name_lower.count("e")

# Form the score
score = int(str(true)+str(love))

# Print the results
if score<10 or score>90:
    print(f"Your score is {score}, you go together like coke and mentos")
elif score>=40 and score<=50:
    print(f"Your score is {score}, you are alright together")
else:
    print(f"Your score is {score}")
