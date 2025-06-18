balance = 30000
passbook = []
def deposit():
    global balance
    deposit_amount = int(input("Enter the amount that you want to deposit: "))
    balance += deposit_amount
    print(f"The balance of your account is {balance} after depositing.")
    passbook.append(f"{deposit_amount} was deposited in the account.")

def withdraw():
    global balance
    withdraw_amount = int(input("Enter the amount that you want to withdraw: "))
    if balance > withdraw_amount:
        balance -= withdraw_amount
        print(f"The balance of your account is {balance} after withdrawing.")
        passbook.append(f"{withdraw_amount} was withdrawn from the account.")
    else:
        print("Insufficient Balance.")

def check_balance():
    global balance
    print(f"Your balance in the account is: {balance}.")

def check_passbook():
    global balance
    print("Passbook logs are: ")
    print(passbook)


options = """1.Deposit Amount
2.Withdraw Amount
3.Check Balance
4.check Passbook
5.Exit"""
tocontinue = True
while tocontinue == True:
    print(options)
    choice = int(input("Enter your choice from the above options: "))
    if choice == 1:
        print(deposit())
    elif choice == 2:
        print(withdraw())
    elif choice == 3:
        print(check_balance())
    elif choice == 4:
        print(check_passbook())
    elif choice == 5:
        tocontinue = False
    else:
        print("Invalid Choice!")