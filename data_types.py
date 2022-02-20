user=input("What is your name?\n")
print(f"my name is {user}")
user_age=int(input("How old are you?\n"))
print(f"I am {user_age} years old")
user_height=float(input("How tall are you?\n"))
print(f"I am {user_height:.2f} meters tall")
user_weight=float(input("How much do you weight?\n"))
bmi=user_weight/user_height**2
print(f"{user} you are {user_age} years old and your bmi is {bmi:.2f}")