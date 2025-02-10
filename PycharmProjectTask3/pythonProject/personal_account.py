from amount import Amount

class PersonalAccount:
    def __init__(self, account_number: int, account_holder: str):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0.0
        self.transactions = []

    def deposit(self, amount: float):
        transaction = Amount(amount, "DEPOSIT")
        self.transactions.append(transaction)
        self.balance += amount

    def withdraw(self, amount: float):
        if amount > self.balance:
            print("Insufficient balance.")
            return
        transaction = Amount(amount, "WITHDRAWAL")
        self.transactions.append(transaction)
        self.balance -= amount

    def print_transaction_history(self):
        print("Transaction History:")
        for transaction in self.transactions:
            print(transaction)

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Account {self.account_number} held by {self.account_holder} with balance ${self.balance:.2f}"
