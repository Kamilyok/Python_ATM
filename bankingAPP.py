'''This app is created by Kamila Kalchakeeva
   based on provided tutorial towards enhancing 
   and showcasing gained skills during
   learning and development phase at Year Up'''
import random
import time
# The following code is a constructor for the app
class Account:
    # Counstruct an Account object
    def __init__(self, id, checking_bal = 0, savings_bal = 0, interest = 3.4):
        self.__id = id
        self.__checking_bal = checking_bal
        self.__savings_bal = savings_bal
        self.__interest = interest
    # Mutator methods
    def setID(self, id):
        self.__id = id
    def set_checking_bal(self, checking_bal):
        self.__checking_bal = checking_bal
    def set_savings_bal(self, savings_bal):
        self.__savings_bal = savings_bal
    # Accessor methods
    def getID(self):
        return self.__id
    def get_checking_bal(self):
        return self.__checking_bal
    def get_savings_bal(self):
        return self.__savings_bal
    def get_interest(self):
        self.__interest
    # Transactions with checking account
    def withdraw_checking(self, amount):
        self.__checking_bal -= amount
    def deposit_checking(self, amount):
        self.__checking_bal += amount
    def transfer_checking(self, amount):
        self.__checking_bal += amount
        self.__savings_bal -= amount
    # Transactions with savings account
    def withdraw_savings(self, amount):
        self.__savings_bal -= amount
    def deposit_savings(self, amount):
        self.__savings_bal += amount
    def transfer_savings(self, amount):
        self.__savings_bal += amount
        self.__checking_bal -= amount

# Following code is an app itself
def main():
    # Creating accounts
    accounts = []
    for i in range(1000, 9999):
        account = Account(i, 0)
        accounts.append(account)
    while True:
        print("Welcome to the BankApp.")
        id = int(input("\nEnter 4-digit account pin: "))
        # Loop till id is valid
        while id < 1000 or id > 9999:
            id = int(input("\nInvalid Id.. Re-enter: "))
        while True:
            # Output menu
            print("\nMenu:")
            print("============================")
            print('1. View Checking Balance')
            print('2. Withdraw Checking')
            print('3. Deposit Checking')
            print('4. Transfer Checking')
            print('5. View Saving Balance')
            print('6. Withdraw Savings')
            print('7. Deposit Savings')
            print('8. Transfer Saving')
            print('0. Exit.')
            # Get menu option from the user
            option = int(input("Enter your numerical selection: "))
            for acc in accounts:
                if acc.getID() == id:
                    user = acc
                    break
            # Option 1 - View Checking Balance
            if option == 1:
                print(f'\nChecking account balance: ${user.get_checking_bal():,.2f}')
                time.sleep(2)
                
            # Option 2 - Withdraw Checking
            elif option == 2:
                # Get the amount to withdraw
                amount = float(input("\nEnter the amount to withdraw from checking: "))
                verify = input(f'Is ${amount:,.2f} the correct amount to withdraw?(Yes/No)')
                verify = verify.upper()
                if verify == 'YES':
                    print("\nVerified checking account withdraw.")
                    time.sleep(2)
                else:
                    break
                if amount < user.get_checking_bal(): 
                    user.withdraw_checking(amount)
                    print(f'Your updated checking balance is ${user.get_checking_bal():,.2f}')
                    time.sleep(2)
                else:
                    print(f'Your checking balance is less than withdrawl amount: ${user.get_checking_bal():,.2f}')
                    time.sleep(2)

            # Option 3 - Deposit to checking.
            elif option == 3:
                amount = float(input("\nEnter the amount to deposit to checking: "))
                verify = input(f'Is ${amount:,.2f} the correct amount to deposit?(Yes/No)')
                verify = verify.upper()
                if verify == 'YES':
                    print("\nVerified checking account deposit.")
                    time.sleep(2)
                    user.deposit_checking(amount)
                    print(f'Your updated checking balance is ${user.get_checking_bal():,.2f}')
                else:
                    break
            
            # Option 4 - Transfer checking
            elif option == 4 :
                amount = float(input("\nEnter amount to transfer from savings account to checking: "))
                verify = input(f'Is ${amount:,.2f} the correct amount to transfer to checking account?(Yes/No)')
                verify = verify.upper()
                if verify == 'YES':
                    print("\nVerified checking account transfer.")
                    time.sleep(2)
                else:
                    time.sleep(2)
                    break
                if amount < user.get_savings_bal():
                    user.transfer_checking(amount)
                    print(f'Your updated checking balance is ${user.get_checking_bal():,.2f}')
                    time.sleep(2)
                else:
                    print(f'\nYour savings account balance is less than transfer amount: ${user.savings_bal():,.2f}')
                    time.sleep(2)
            
            # Option 5 - View Savings balance
            elif option == 5:
                print(f'\nSavings account balance: ${user.get_savings_bal():,.2f}')
                time.sleep(2)
            
            # Option 6 - Withdraw Savings
            elif option == 6:
                # Get the amount to withdraw
                amount = float(input("\nEnter the amount to withdraw from savings: "))
                verify = input(f'Is ${amount:,.2f} the correct amount to withdraw?(Yes/No)')
                verify = verify.upper()
                if verify == 'YES':
                    print("\nVerified checking account withdraw.")
                    time.sleep(2)
                else:
                    break
                if amount < user.get_savings_bal(): 
                    user.withdraw_savings(amount)
                    print(f'Your updated savings balance is ${user.get_savings_bal():,.2f}')
                    time.sleep(2)
                else:
                    print(f'Your savings balance is less than withdrawl amount: ${user.get_savings_bal():,.2f}')
                    time.sleep(2)
                
            # Option 7 - Deposit to checking.
            elif option == 7:
                amount = float(input("\nEnter the amount to deposit to savings: "))
                verify = input(f'Is ${amount:,.2f} the correct amount to deposit?(Yes/No)')
                verify = verify.upper()
                if verify == 'YES':
                    print("\nVerified checking account deposit.")
                    time.sleep(2)
                    user.deposit_savings(amount)
                    print(f'Your updated savings balance is ${user.get_savings_bal():,.2f}')
                    time.sleep(2)
                else:
                    break
                    time.sleep(2)
            # Option 8 - Transfer savings
            elif option == 8 :
                amount = float(input("\nEnter amount to transfer from checking account to savings: "))
                verify = input(f'Is ${amount:,.2f} the correct amount to transfer to savings account?(Yes/No)')
                verify = verify.upper()
                if verify == 'YES':
                    print("\nVerified saving account transfer.")
                    time.sleep(2)
                else:
                    time.sleep(2)
                    break
                if amount < user.get_checking_bal():
                    user.transfer_savings(amount)
                    print(f'Your updated savings balance is ${user.get_savings_bal():,.2f}')
                    time.sleep(2)
                else:
                    print(f'\nYour checking account balance is less than transfer amount: ${user.checking_bal():,.2f}')
                    time.sleep(2)
            # Exiting the program
            elif option == 0:
                print("\nTransaction is now complete.")
                print("Transaction number: ", random.randint(10000,1000000))
                print("Thanks for choosing us as your bank")
                exit()
            else:
                print("\nThat's an invalid choice.")
                break
if __name__ == "__main__":
    main()
