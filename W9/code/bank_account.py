class BankAccount:
    """A bank account with an owner and a balance."""
  
    def __init__(self, name: str, balance: float = 0.0) -> None:
        """Create an account for 'name' as owner ad with a starting balance."""
        self.owner = name
        self.balance = balance
    
    def deposit(self, amount: float) -> None:
        """Add amount to this account's balance."""
        if amount < 0:
            print("Invalid amount")
        else:
            self.balance += amount
    
    def get_balance(self)-> float:
        return self.balance
    
    def interest_earned(self, rate: float) -> float:
        """Return one period of interest at rate, without adding it."""
        return round(self.balance * rate, 2)
    
    def can_afford(self, amount: float) -> bool:
        """Return True if the balance covers amount."""
        if self.balance >= amount:
            return True
        return False
    
    def withdraw(self, amount: float) -> bool:
        """Remove amount if the balance covers it and return True. 
        Otherwise, return false."""
        if not self.can_afford(amount):
            #raise ValueError("amount not covered by balance!")
            return False
        self.balance -= amout
        return True
    




    




    
