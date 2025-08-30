print("Welcome to Slayer's Coffee Shop")

print("Menu:")
print("1. Espresso - ₹100")
print("2. Black Coffee - ₹150")
print("3. Latte - ₹120")
print("4. Mocha - ₹180")

choice = int(input("Choose your coffee: "))

# First order variables
coffee = ""
price = 0

if choice == 1:
    coffee = "Espresso"
    price = 100
elif choice == 2:
    coffee = "Black Coffee"
    price = 150
elif choice == 3:
    coffee = "Latte"
    price = 120
elif choice == 4:
    coffee = "Mocha"
    price = 180
else:
    print("Invalid order")
    exit()  # stop program if choice is invalid

quantity = int(input(f"How many cups of {coffee} do you want? "))

# For add-on
add_on = input("Do you want to order more (yes or no)? ").lower()

# Second order variables
price1 = 0
coffee1 = ""
quantity1 = 0

if add_on == "yes":
    choice1 = int(input("What is your next order: "))
    quantity1 = int(input("How many cups do you want? "))

    if choice1 == 1:
        coffee1 = "Espresso"
        price1 = 100
    elif choice1 == 2:
        coffee1 = "Black Coffee"
        price1 = 150
    elif choice1 == 3:
        coffee1 = "Latte"
        price1 = 120
    elif choice1 == 4:
        coffee1 = "Mocha"
        price1 = 180
    else:
        print("Invalid choice for second order, proceeding with first order only.")
        quantity1 = 0

elif add_on == "no":
    print("Proceeding with first order only.")

else:
    print("Invalid input for add-on, proceeding with first order only.")

# For Bill
bill = price * quantity + price1 * quantity1

# Print order summary
print(f"You ordered {quantity} {coffee}", end="")
if quantity1 > 0:
    print(f" and {quantity1} {coffee1}")
else:
    print(".")

print("Your total bill is ₹", bill)
