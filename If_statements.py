#if = Do some code only if some condition is True Else do something else

for_sale = True

if for_sale:
    print("Thios item is for sale")
else:
    print("This item is NOT for sale")



name = input("Enter your name: ")

if name == "":
    print("You did not type in your name")
else:
    print(f"hello {name}")

response = input("Would you like food? (Y/N): ")

if response == "Y":
    print("Have some food")
else:
    print("No food for you!")


age = int(input("Enter your age: "))

if age >= 100:
    print("You are too old to be signed up")
elif age >= 18:
    print("You are now signed up!")
elif age <= 0:
    print("You haven't been born yet!")
else:
    print("You must be 18+ to be sign up")



