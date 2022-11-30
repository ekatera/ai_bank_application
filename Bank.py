from Customer import Customer
from Account import Account
from Datasource import Datasource

class Bank(Datasource):
    # class initialization
    def __init__(self):
        Datasource.__init__(self)

    # add new customer
    # with unique pnr number
    def add_customer(self, name, pnr):
        if self._check_pnr_unique(pnr):
            self.customers.append(Customer(name, pnr))
            print(f"Customer with id {pnr} and name {name} was successfully added")
            return True
        print(f"Customer with id {pnr} and name {name} was NOT added. Probably the customer with this id already exists.")
        return False

    # add account to existing Customer
    def open_account(self, pnr):
        customer = self.get_customer_by_id(pnr)
        if customer:
            customer.create_account(self._generate_account_number())
            return True
        print(f"Could not add account for customer with personal number {pnr}. Customer is not found.")
        return False

    def deposit(self, pnr, account_id, amount):
        customer = self.get_customer_by_id(pnr)
        if customer:
            account = customer.get_account(account_id)
            if account:
                account.deposit(amount)
                self.transaction_file.writelines(f"customer id: {customer._pnr} account {account.account_id} \n {str(account.last_transaction)}\n")
            else:
                print(f"Customer with id {pnr} does not have account with id {account_id}")
        else:
            print(f"Customer with id {pnr} does not exist")

    def withdraw(self, pnr, account_id, amount):
        customer = self.get_customer_by_id(pnr)
        if customer:
            account = customer.get_account(account_id)
            if account:
                if account.withdraw(amount):
                    self.transaction_file.writelines(f"customer id: {customer._pnr} account {account.account_id} \n {str(account.last_transaction)}\n")
            else:
                print(f"Customer with id {pnr} does not have account with id {account_id}")
        else:
            print(f"Customer with id {pnr} does not exist")

    def close_account(self, customer_id, account_id):
        customer = self.get_customer_by_id(customer_id)
        if customer:
            customer.remove_account(account_id)
        else:
            print(f"Customer with customer id {customer_id} was not found.")

    def print_customer(self, pnr):
        customer = self.get_customer_by_id(pnr)
        if customer:
            customer.print_info()

    def print_all_customers(self):
        for customer in self.customers:
            customer.print_info()

    # check customer transaction
    def print_customer_transactions(self, customer_id=None):
        if customer_id:
            customer = self.get_customer_by_id(customer_id)
            if customer:
                customer.print_transactions()
        else:
            for customer in self.customers:
                customer.print_transactions()
