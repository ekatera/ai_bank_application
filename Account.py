from Transactions import Transactions

class Account(Transactions):
    def __init__(self, account_id, account_type="1", balance=0):
        self.account_id = int(account_id)
        self.account_type = str(account_type)
        self.balance = int(balance)
        Transactions.__init__(self)

    # print account info
    def print_account(self):
        account_info = f"Account id is {self.account_id}\nAccount type is {self.account_type}\n"\
                       f"Balance is {self.balance}.\n"
        print(account_info)
        return account_info


    def deposit(self, amount):
        self.balance += int(amount)
        self.add_transaction("deposit", amount)
        print(f"{amount} was added to account {self.account_id}")

    def withdraw(self, amount):
        if self.balance > int(amount):
            self.balance -= int(amount)
            self.add_transaction("withdraw", amount)
            return True
        else:
            print(f"Operation withdraw {amount} cannot be completed for {self.account_id}, the amount is higher then available amount")
            return False