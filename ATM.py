class ATM:
    '''ATM class'''

    def __init__(self):
        self.balance = 0


    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError('Deposit amount must be positive.')
        self.balance += amount
        return True

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError('Insufficient funds.')
        if amount <= 0:
            raise ValueError('Withdrawal amount must be positive.')
        self.balance -= amount
        return True
    
def get_number(prompt):
    while True:
        try:
            number = float(input(prompt))
            return number
        except ValueError:
            print("Invalid input. Please enter a number.")


def main():
    atm = ATM()
    while True:
        print('\n WELCOME TO ATM MACHINE')
        print('1. Check Balance')
        print('2. Deposit')
        print('3. Withdraw')
        print('4. Exit')

        choice = input('Please choose an option: ')

        if choice == '1':
            balance = atm.check_balance()
            print(f'Your current balance is ${balance}')

        elif choice == '2':
            while True:
                try:
                    amount = get_number('Enter the amount to deposit: ')
                    atm.deposit(amount)
                    balance = atm.check_balance()
                    print(f'Deposited ${amount}. Your new balance is ${balance}')
                    break
                except ValueError as e:
                    print(f'Error: {e}')

        elif choice == '3':
            while True:
                try:
                    amount = get_number('Enter the amount to withdraw: ')
                    atm.withdraw(amount)
                    balance = atm.check_balance()
                    print(f'Withdrew ${amount}. Your new balance is ${balance}')
                    break
                except ValueError as e:
                    print(f'Error: {e}')

        elif choice == '4':
            print('Goodbye! thank you for using ATM')
            break

        else:
            print('Invalid option. Please choose a valid option.')


if __name__ == '__main__':
    main()
