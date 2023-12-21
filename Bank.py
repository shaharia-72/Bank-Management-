import random
# import hashlib
from User import User
from Admin import Admin


class Bank:
    def __init__(self):
        self.users = []
        self.total_balance = 0
        self.total_loan_balance_amount = 0
        self.loan_feature_enabled = True

# ! account number
    def generate_account_number(self):
        return random.randint(100, 999)

# ! user account
    def create_user_account(self, name, email, address, account_type, initial_balance):
        account_number = self.generate_account_number()

        new_user = User(account_number, name, email, address,
                        account_type, initial_balance)
        self.users.append(new_user)

        print(f"Account created successfully for {
            new_user.name} with account_number: {new_user.account_number}")

        return new_user

# ! delete account
    def delete_account(self, account_number):

        user = self.get_user(account_number)
        if user:
            self.users.remove(user)
            print(f"this account: {account_number} has been deleted")
        else:
            print("This account not exist")

# ! find user by account number

    def get_user(self, account_number):
        for user in self.users:
            if user.account_number == account_number:
                return user
        return None

# ! display all account

    def display_all_accounts(self):
        if not self.users:
            print("No active user found: add new user by admin")
            return

        print("======= ALL USER ACCOUNTS =======")
        for user in self.users:
            if isinstance(user, Admin):
                continue

            print(f"Account number: {user.account_number}, Name: {user.name}, Address: {
                  user.address}, Balance: ${user.check_balance():.2f}")

# ! total balance of all accounts

    def bank_total_balance(self):
        total_balance = sum(user.check_balance()
                            for user in self.users if not isinstance(user, Admin))
        return total_balance

# ! total loan balance

    def give_loan_amount(self):
        return self.total_loan_balance_amount

# ! loan feature

    def ON_OFF_loan_feature(self, status):
        self.loan_feature_enabled = status
        print(f"Loan Feature is {'ON' if status else 'OFF'}")
