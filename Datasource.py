
class Datasource:
    def __init__(self):
        self.customers = []
        self._last_generated_account = 1000
        self.transaction_file = open("transactions.txt", "w")

    # help function to find customer with given id
    def get_customer_by_id(self, pnr):
        for customer in self.customers:
            if customer.get_pnr() == int(pnr):
                return customer
        return None

    # check there is no customer with given pnr
    def _check_pnr_unique(self, pnr):
        if self.get_customer_by_id(int(pnr)) is None:
            return True
        return False

    # change customer's name
    # id is not changeable
    def change_customer_name(self, name, pnr):
        customer = self.get_customer_by_id(pnr)
        if customer:
            customer.set_name(name)
            print(f"Customer with personal number {pnr} was successfully renamed to {name}.")

    # remove customer
    # and account
    def remove_customer(self, pnr):
        customer = self.get_customer_by_id(pnr)
        if customer:
            self.customers.remove(customer)
            print(f"Customer with personal number {pnr} was successfully deleted.")
        else:
            print(f"Could not find customer with personal number {pnr}.")

    # generate next account number
    def _generate_account_number(self):
        self._last_generated_account += 1
        return self._last_generated_account