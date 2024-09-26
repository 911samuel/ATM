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
    
class ATMController:
    '''ATM controller class'''

    def __init__(self) -> None:
        self.atm = ATM()

    def get_number(self,prompt):
        while True:
            try:
                number = float(input(prompt))
                return number
            except ValueError:
                print("Invalid input. Please enter a number.")
    
    def display(self):
        while True:
            print('\n WELCOME TO ATM MACHINE')
            print('1. Check Balance')
            print('2. Deposit')
            print('3. Withdraw')
            print('4. Exit')

    def check_balance(self):
        balance = self.atm.check_balance()
        print(f'Your current balance is ${balance}')

    def deposit(self):
        while True:
            try:
                amount = self.get_number('Enter the amount to deposit: ')
                self.atm.deposit(amount)
                balance = self.atm.check_balance()
                print(f'Deposited ${amount}. Your new balance is ${balance}')
                break
            except ValueError as e:
                print(f'Error: {e}')

    def withdraw(self):
        while True:
            try:
                amount = self.get_number('Enter the amount to withdraw: ')
                self.atm.withdraw(amount)
                balance = self.atm.check_balance()
                print(f'Withdrew ${amount}. Your new balance is ${balance}')
                break
            except ValueError as e:
                print(f'Error: {e}')

    def run(self):
        while True:
            self.display()
            choice = input('Please choose an option: ')

            if choice == '1':
                self.check_balance()
            elif choice == '2':
                self.deposit()
            elif choice == '3':
                self.withdraw()
            elif choice == '4':
                print('Goodbye! thank you for using ATM')
                break
            else:
                print('Invalid option. Please choose a valid option.')





def main():
    atm_controller = ATMController()
    atm_controller.run()

    
if __name__ == '__main__':
    main()
