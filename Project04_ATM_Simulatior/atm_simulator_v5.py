
def show_menu():
    print("=" * 40)
    print("             ATM Menu")
    print("=" * 40)

    print("\n1. Check Balance")
    print("2. Withdraw")
    print("3. Deposit")
    print("4. Exit")

def check_balance(balance):
    print("Current Balance: ", balance)

def withdraw(balance):
    withdrawal_amount = int(input("Withdrawal Amount: "))

    if withdrawal_amount <= 0:
        print("Invalid Withdrawal Amount!") 
    
    elif withdrawal_amount > balance:
        print("Insufficient Balance!")
    
    else:
        balance -= withdrawal_amount
        print("Transaction Successful!")
        print("Remaining Balance: ", balance)

    return balance

def deposit(balance):
    deposit_amount = int(input("Deposit Amount: "))

    if deposit_amount <= 0:
        print("Invalid Deposit Amount!")

    else:
        balance += deposit_amount
        print("New Balance: ", balance)

    return balance

balance = 5000  


while True:

    show_menu()

    menu_choice = int(input("Choose an option: "))

    if menu_choice == 1:
        check_balance(balance)

    elif menu_choice == 2:
        balance = withdraw(balance)

    elif menu_choice == 3:
        balance = deposit(balance)

    elif menu_choice == 4:
        print("Exiting ATM...")
        break

    else:
        print("Invalid Option!")

print("=" * 40)
print("Thank you for using our ATM!")
print("=" * 40)