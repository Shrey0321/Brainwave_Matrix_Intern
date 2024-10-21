class ATM:
    def __init__(self):
        self.balance = 1000  # Initial balance
        self.pin = "1234"    #PIN
        self.transaction history []

    def display_menu(self):
        print("\nATM Interface")
        print("1. Check Balance")
        print("2. Deposit Cash")
        print("3. Withdraw Cash")
        print("4. View Transaction history")
        print("5. change pin ")
        print("6. exit")

    def check_balance(selfxx bn):
        print(f"Your current balance is: ${self.balance}")

    def deposit_cash(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"You have deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw_cash(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"You have withdrawn ${amount}. New balance: ${self.balance}")
        elif amount > self.balance:
            print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Select an option (1-4): ")

            if choice == '1':
                self.check_balance()
            elif choice == '2':
                amount = float(input("Enter amount to deposit: "))
                self.deposit_cash(amount)
            elif choice == '3':
                amount = float(input("Enter amount to withdraw: "))
                self.withdraw_cash(amount)
            elif choice == '4':
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")

if __name__ == "__main__":
    atm = ATM()
    atm.run()
