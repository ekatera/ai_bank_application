import datetime
class Transactions:
    def __init__(self):
        self.transactions = []
        self.last_transaction = None

    def _get_timestamp(self):
        date_time = datetime.datetime.now()
        time_to_str = date_time.strftime("%d-%b-%Y %H:%M:%S.%f")
        return time_to_str

    def add_transaction(self, operation_type, amount):
        self.last_transaction = {"Opeation type": operation_type, "Amount":amount, "Operation time":self._get_timestamp()}
        self.transactions.append(self.last_transaction)

    def print_transaction(self):
        if not len(self.transactions):
            return "     No transactions were made for this account\n\n"
            return
        for transaction in self.transactions:
            print(f"       {transaction}")
