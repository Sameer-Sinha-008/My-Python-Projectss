class BankAccount:
    def __init__(self, name, initial_deposit, pin):
        self.account_holder = name #public
        self.__balance = initial_deposit  #private
        self.__pin = pin #private
    #1. Balance Check Method
    def check_balance(self, entered_pin):
        if entered_pin == self.__pin:
            print(f"Account Holder: {self.account_holder}")
            print(f"Current Balance: ₹{self.__balance}")
        else:
            print("Access Denied! Enter the Right Pin")
    #2. Deposit method
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"\n₹{amount: .2f} Successfully Deposited!")
            print(f"\nNew Balance: ₹{self.__balance: .2f}")
        else:
            print("Invalid Deposit Amount!")
    #3. Withdraw method
    def withdraw(self, amount, entered_pin):
        if entered_pin != self.__pin:
            print("\n Incorrect Pin! Transaction Failed!")
            return
        if amount <= 0:
            print("\n Invalid Withdraw Amount!")
        elif amount > self.__balance:
            print(f"\n Insufficient Balance! Available: ₹{self.__balance: .2f}")
        else:
            self.__balance -= amount
            print(f"\n Please Collect Your Cash: ₹{amount: .2f}")
            print(f"Remaining Balance: ₹{self.__balance: .2f}")

#ATM :)
def start_atm():
    print("===========================================================")
    print("            WELCOME TO SMART PYTHON BANK")
    print("===========================================================")
    
    name = input("Enter Account Holder Name: ")
    initial_money = float(input("Enter Initial.Deposit (₹): "))
    pin = int(input("Set a 4-Digit PIN: "))

    user_account = BankAccount(name, initial_money, pin)
    print("\n Account Created Successfully!")
    
    while True:
        print("\n-----------------------------------------------------------")
        print("1. Check Balance")
        print("2. Check Deposit Money")
        print("3. Check Withdraw Money")
        print("4. Exit ATM")
        print("\n------------------------------------------------------------")
        choice = input("Select Option (1-4): ")
        
        if choice == "1":
            check_pin = int(input("Enter the PIN: "))
            user_account.check_balance(check_pin)
        elif choice == "2":
            amt = float(input("Enter Deposit Amount (₹): "))
            user_account.deposit(amt)
        elif choice == "3":
            amt = float(input("Enter Withdraw Amount (₹): "))
            check_pin = int(input("Enter Pin: "))
            user_account.withdraw(amt, check_pin)
        elif choice == "4":
            print("\n Thank You For Banking With Us! Have a Great Day!")
            break
        
        else:
            print("\n Invalid Option! Please Choose 1-4. ")
            
start_atm()
