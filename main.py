from venv.Account import Account
from venv.Customer import Customer
from venv.Bank import Bank

if __name__ == '__main__':
    bank = Bank()
    customer_id = 55

    # Create a group of 6 customers and open accounts for them
    for customer_name in ["Alex", "Victor", "Lisa", "Anna", "Vera", "Stefan", "Peter"]:
        bank.add_customer(customer_name, customer_id)
        bank.open_account(customer_id)
        customer_id += 1

    # try to add a new customer with existing pnr
    bank.add_customer("Jon", 56)
    bank.print_all_customers()
    # remove existing customer
    bank.remove_customer(57)

    # remove customer that does not exist
    bank.remove_customer(12)
    bank.print_all_customers()

    # rename existing customer
    bank.change_customer_name("Peter M", "61")

    # open one more account for existing customer
    bank.open_account(61)
    bank.print_customer(61)

    # open account for a customer that does not exist
    bank.open_account(1002)

    # account does not exist
    bank.close_account(60, 1007)
    # close existing account
    bank.close_account(60, 1006)


    bank.print_all_customers()

    # make deposit to existing customer and existing account
    bank.deposit(58, 1004, 50)
    bank.deposit(58, 1004, 50)
    bank.withdraw(58, 1004, 50)

    bank.withdraw(61, 1007, 50)
    # make deposit to existing customer and unknown account
    bank.deposit(60, 1005, 1450)

    bank.print_customer_transactions(58)
    bank.print_customer_transactions()