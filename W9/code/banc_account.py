class BankAccount:
    """A bank account with an owner and a balance."""
  
    def __init__(self, name: str, balance: float = 0.0) -> None:
        """Create an account for 'name' as owner ad with a starting balance."""
        self.owner = name
        self.balance = balance

    
