from Account import Account

class CustomerException(Exception):
    pass

class Customer(Account):
    def __init__(self, name, pnr):
        self._name = str(name)
        self._pnr = int(pnr)
        self.customer_accounts = []

    def set_name(self, new_name):
        self._name = new_name

    def get_pnr(self):
        return self._pnr

    def print_info(self):
        print(f"\n\nCustomer name is {self._name} with id {self._pnr}")
        for account in self.customer_accounts:
            account.print_account()
        return [self._name, self._pnr]

    def create_account(self, account_id):
        self.customer_accounts.append(Account(account_id))
        print(f"account with account id {account_id} was successfully added for customer {self._name} with id {self._pnr}")

    def get_account(self, account_id):
        for account in self.customer_accounts:
            if int(account.account_id) == int(account_id):
                return account

    def remove_account(self, account_id):
        account = self.get_account(account_id)
        if account:
            self.customer_accounts.remove(account)
            print(f"Account with id {account_id} was successfully deleted from {self._name} and id {self._pnr}")
        else:
            print(f"Account with id {account_id} was not found for customer {self._name} with id {self._pnr}")

    def print_transactions(self):
        print(f"\nTransactions for customer {self._name} with id {self._pnr}")
        for account in self.customer_accounts:
            print(f"Transactions for account {account.account_id}")
            account.print_transaction()
