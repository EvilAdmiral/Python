user_id = "admin05"
Name = "Gagan"
Account_Balance = 147800
correct_pin = "0525"

print("===== Welcome to the ATM =====")

entered_user_id = input("Enter your User ID: ")

if entered_user_id != user_id:
    print("Invalid User ID. Access Denied.")
else:
    entered_pin = input("Enter your PIN: ")

    if entered_pin != correct_pin:
        print("Invalid PIN. Access Denied.")
    else:
        print(f"\nWelcome, {Name} (User ID: {user_id})")

        while True:
            print("\n===== ATM Menu =====")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Exit")

            choice = input("Enter your choice (1-4): ")

            if choice == '1':
                print(f"Your current balance is: {Account_Balance}")

            elif choice == '2':
                deposit_amount = float(input("Enter amount to deposit: "))
                if deposit_amount <= 0:
                    print("Invalid amount. Please enter a positive value.")
                else:
                    Account_Balance += deposit_amount
                    print(f"{deposit_amount} deposited successfully. New balance: {Account_Balance}")

            elif choice == '3':
                withdraw_amount = float(input("Enter amount to withdraw: "))
                if withdraw_amount <= 0:
                    print("Invalid amount. Please enter a positive value.")
                elif withdraw_amount > Account_Balance:
                    print(f"Insufficient balance. Your current balance is: {Account_Balance}")
                else:
                    Account_Balance -= withdraw_amount
                    print(f"{withdraw_amount} withdrawn successfully. New balance: {Account_Balance}")

            elif choice == '4':
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")
