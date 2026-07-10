balance = 5000

print("=" * 40)
print("     ATM Simulator")
print("=" * 40)

print("Current Balance: ", balance)


cash_withdrawal = int(input("Enter your withdrawal amount:  "))

if cash_withdrawal <= balance:
    print("Transaction Successful! \nRemaining Balance:", balance - cash_withdrawal)
else:
    print("Insufficient Balance!")

print("=" * 40)
print("Thank you for using our ATM!")
print("=" * 40)