from Bank import Bank
from Admin import Admin
from User import User


def main():
    bank = Bank()
    admin = Admin()

    user_1 = bank.create_user_account(
        "user1", "user1@gmail.com", "Banglabazer", "Savings", 5000)
    user_1.create_password("user1")
    user_1.account_number = 123
    # bank.display_all_accounts(account_number)

    user_2 = bank.create_user_account(
        "user2", "user2@gmail.com", "Banglabazer", "Savings", 5000)
    user_2.create_password("user2")
    user_2.account_number = 1234

    while True:
        print("======= Banking Management System =======")
        print("\nOnly admin can create accounts")

        print("\n1. User login")
        print("\n2. Admin login")
        print("\n3. Exit")

        choice = input("\nEnter your choice from 1/2/3: ")

        if choice == "1":
            user_panel(bank)
        elif choice == "2":
            admin_panel(admin, bank)
        elif choice == "3":
            print("Exiting............")
            break
        else:
            print("Invalid choice")


def user_panel(bank):
    print("\n======= User Menu =======")

    account_number = input("Enter your account number: ")
    if account_number.isdigit():
        user = bank.get_user(int(account_number))
    else:
        print("Account not found.....")
        return

    if not user:
        print("Account not found.........")
        return

    if user:
        if not user.password:
            print(
                "This time you try to enter first time in your account. for that you need to set a password")
            user.create_password(input("Enter your password: "))
        # elif user.password is True:
        #     password = input("Enter your password: ")
        #     user.create_password(password)
        else:
            password = input("Enter your password: ")
            if not user.check_password(password):
                print("Incorrect password. Please try again")
                return

        while True:
            print("\n1. Deposit")
            print("2. Withdraw")
            print("3. See balance")
            print("4. Transaction history")
            print("5. Take loan")
            print("6. Transfer amount")
            print("7. Back to main menu")

            choice = input("Enter your choice:   ")

            if choice == "1":
                amount = float(input("Enter the deposit amount: "))
                user.deposit_amount(amount)
            elif choice == "2":
                amount = float(input("Enter the withdraw amount: "))
                user.withdraw_amount(amount)
            elif choice == "3":
                print(f"current balance: ${user.check_balance()}")
            elif choice == "4":
                user.transaction_history()
            elif choice == "5":
                amount = float(input("Enter the loan amount: "))
                user.loan(amount, bank)
            elif choice == "6":
                receiver = int(
                    input("Enter the receiver account number: "))
                amount = float(input("Enter the amount to transfer: "))
                user.transfer_balance(amount, receiver, bank)
            elif choice == "7":
                # print("Invalid choice. Please try again")
                break
    else:
        print("User not found. Enter correct account number.")


def admin_panel(admin, bank):
    print("\n======= Admin Panel =======")

    password = input("Enter password: ")

    if admin.check_password(password):
        while True:
            print("\n1. Add account")
            print("2. delete account")
            print("3. Display all accounts")
            print("4. Total balance")
            print("5. total loan balance")
            print("6. Turing off/on loan features")
            print("7. Back to main menu")

            admin_choice = input("Enter your operation:  ")

            if admin_choice == "1":
                name = input("Enter the new user name: ")
                email = input("Enter the new user email address: ")
                address = input("Enter the new user address: ")
                account_type = input(
                    "Enter the new user account type (savings/current): ")
                bank.create_user_account(
                    name, email, address, account_type, initial_balance=0)
            elif admin_choice == "2":
                account_number = int(
                    input("Enter the user number that you need to delete"))
                bank.delete_account(account_number)
            elif admin_choice == "3":
                bank.display_all_accounts()
            elif admin_choice == "4":
                print(f"Total balance: ${bank.bank_total_balance()}")
            elif admin_choice == "5":
                print(f"Total give loan balance: ${
                    bank.give_loan_amount()}")
            elif admin_choice == "6":
                status = input("Enter status (ON/OFF): ").upper()
                bank.ON_OFF_loan_feature(status == "ON")
            elif admin_choice == "7":
                break
            else:
                print("Invalid choice. Please try again.")
    else:
        print("wrong password")


if __name__ == "__main__":
    main()
