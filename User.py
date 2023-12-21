# from Bank import bank_total_balance
import hashlib


class User:
    def __init__(self, account_number, name, email, address, account_type, initial_deposit):

        self.account_number = account_number
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.balance = initial_deposit
        self.transaction_history_list = []
        self.loan_taken = 0
        self.password = None

# ! create password

    def create_password(self, password):
        self.password = hashlib.sha256(password.encode()).hexdigest()
        print(f"Password is successfully set for this account: {
              User.set_password}")


# ! set password


    def set_password(self, password):
        self.password = hashlib.sha256(password.encode()).hexdigest()
        print(f"Password is successfully set for this account: {
              User.set_password}")

# ! check password
    def check_password(self, password):
        return self.password == hashlib.sha256(password.encode()).hexdigest()

# ! deposit amount
    def deposit_amount(self, amount):
        # from Bank import Bank
        self.balance += amount
        print(f"your current balance: {self.balance}")
        # bank_total_amount += amount
        self.transaction_history_list.append(f" Deposited ${amount}")

# ! withdraw
    def withdraw_amount(self, amount):
        minimum_balance = 500
        if (amount+minimum_balance) > self.balance:
            print(f"Insufficient funds. you need to keep at last ${
                  minimum_balance} in your account")

        else:
            # from Bank import Bank
            self.balance -= amount
            # Bank.bank_total_amount -= amount
            print(f"your current balance: {self.balance}")
            self.transaction_history_list.append(f"Withdraw ${amount}")

# ! check balance

    def check_balance(self):
        return self.balance

# ! def transaction_history

    def transaction_history(self):
        for transaction in self.transaction_history_list:
            print(transaction)

# ! loan

    def loan(self, amount, bank):
        if bank.ON_OFF_loan_feature:
            if self.loan_taken < 2:
                self.loan_taken += 1
                self.balance += amount
                bank.total_loan_balance_amount += amount
                self.transaction_history_list.append(f"Loan taken: ${amount}")
                print(f"Loan has taken successfully")
            else:
                print("You have already taken maximum amount by loan")
        else:
            print("Loan feature is off by admin")

# ! transfer balance

    def transfer_balance(self, amount, receive_account_number, bank):
        receiver = bank.get_user(receive_account_number)
        if receiver:
            if self.balance >= amount:
                self.balance -= amount
                receiver.balance += amount
                self.transaction_history_list.append(
                    f"Transferred ${amount} to this account {receiver.account_number}")
                print("Transferred successfully")
            else:
                print("Balance is not sufficient")
        else:
            print("Account is not available")
