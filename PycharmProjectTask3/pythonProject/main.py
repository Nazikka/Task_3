from personal_account import PersonalAccount

def main():
    account = PersonalAccount(12345, "Nazik")

    print("Initial Account Information:")
    print(account)

    # Deposit money
    account.deposit(1000)
    print(f"\nBalance after deposit: ${account.get_balance():.2f}")

    # Withdraw money
    account.withdraw(300)
    print(f"\nBalance after withdrawal: ${account.get_balance():.2f}")

    # Print transaction history
    print("\nTransaction History:")
    account.print_transaction_history()

if __name__ == "__main__":
    main()


