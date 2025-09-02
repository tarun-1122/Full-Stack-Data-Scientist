correct_pin = 1234
balance = 5000

entered_pin = int(input("Enter your PIN: "))

if entered_pin == correct_pin:
    print("PIN Verified.")
    withdraw_amount = int(input("Enter amount to withdraw: "))
    
    if withdraw_amount <= balance:
        balance -= withdraw_amount
        print(f"Withdrawal Successful. Remaining Balance = {balance}")
    else:
        print("Insufficient Balance.")
else:
    print("Invalid PIN.")
