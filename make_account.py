def make_account(initial_balance):
    if initial_balance < 0:
        raise ValueError("Initial balance cannot be negative.")

    balance = initial_balance

    def deposit(amount):
        nonlocal balance
        try:
            if amount <= 0:
                raise ValueError("Deposit must be positive.")
            balance = balance + amount
            return balance
        except ValueError:
            raise ValueError("Deposit amount must be a number.")

    def withdraw(amount):
        nonlocal balance
        try:
            if amount <= 0:
                raise ValueError("Withdrawal must be positive.")
            if amount > balance:
                raise ValueError("Insufficient funds.")
            balance = balance - amount
            return balance
        except ValueError:
            raise ValueError("Withdrawal amount must be a number.")

    return deposit, withdraw

