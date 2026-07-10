print("=" * 40)
print("             ATM Menu")
print("=" * 40)

balance = 5000


print("\n1. Check Balance")
print("2. Withdraw")
print("3. Deposit")
print("4. Exit")

menu_choice = int(input("Choose an option: "))

if menu_choice <= 0:
    print("Invalid Option")
elif menu_choice > 4:
    print("Invalid Option") 
elif menu_choice == 1:
    print("Balance: ", balance)
elif menu_choice == 2:
    withdrawal = int(input("Withdrawal Amount: "))
    if withdrawal <= 0:
        print("Invalid Request!")
    elif withdrawal > balance:
        print("Insufficient Balance!")
    else:
        balance -= withdrawal
        print("Transaction Successful!")
        print("Remaining Balance: ", balance)

elif menu_choice == 3:
    deposit = int(input("Deposit Amount: "))
    balance += deposit

    print("Balance: ", balance)
else:
    print("Exiting ATM...")

print("=" * 40)
print("Thank you for using our ATM!")
print("=" * 40)