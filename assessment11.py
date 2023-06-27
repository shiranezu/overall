class BankAccount:
    def __init__(self, account_number, account_holder_name, account_type, balance=0):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.account_type = account_type
        self.balance = balance
        self.transaction_history = []
    def deposit(self, amount):
        self.balance+=amount
        self.transaction_history.append(f'you deposited{amount}')
        return 'successful'

    def withdraw(self, amount):
        if self.balance>=amount:
            self.balance-=amount
            self.transaction_history.append(f'you withdrew {amount}')
        else:
            print('you are unable to withdraw due to insufficient balance')

    def current_balance(self):
        return (f"{self.account_holder_name} has {self.balance} remaining")
    
    def transaction (self):
        return self.transaction_history




accounts=[]
def main():
    while True:
        print('Select an option')
        print('1. Create an account')
        print('2. Deposit funds')
        print('3. Withdraw funds')
        print('4. Get balance')
        print()
        response = int(input(''))

        if response == 1:
            name =input('Enter your name')
            new_account = BankAccount(9127571600, name, 'savings', 20000000)
            accounts.append(new_account)
            print('account created successfully')
        elif response == 2:
            name = input('Enter your name')
            for account in accounts:
                if account.account_holder_name == name:
                    amount= int(input('please enter your amount: '))
                    
                    print(account.deposit(amount))
                    break
                else:
                    print(' insufficient amount')
        elif response == 3:
            name = input('Please enter name')
            for account in accounts:
                if name == account.account_holder_name:
                    withdraw_amount = int(input('amount to withdraw:'))
                    account.withdraw(withdraw_amount)
                    print(' withdrawal confirmed')
                    break
                else:
                    print('withdrawal failed')
        elif response == 4:
            name = input('enter your name')
            for account in accounts:
                if name == account.account_holder_name:

                    print(account.current_balance())
main()