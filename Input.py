#input() = A function that prompts the user to enter data and returns the entered data

#Excercise 2 Shopping Cart Program

item = input("What item would like to buy?: ")
price = float(input("What is the price?: "))
quantity = int(input("How many would you like?: "))

total = price * quantity

print(f"You have bought {quantity} x {item}/s")
print(f"Your total is ${total}") 

#Excercise 1 Rectangle Area Calc

length = float(input("Enter the length: "))
width = float(input("Enter the width: "))

area = length * width

print(f"The area is: {area}cm")

name = input("What is your name? :")
age = int(input("How old are you?: "))


age = age + 1

print(f"hello {name}!")
print("Happy Birthday")
print(f"you are {age} years old")


