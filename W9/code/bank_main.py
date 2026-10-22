from bank_account import *

#Client Program

def main() -> None:
    """Open two accounts and show them."""
    ada = BankAccount("Ada", 100.0)
    bo = BankAccount("Bo")
  
    print(ada.owner, ada.balance)
    print(bo.owner, bo.balance)

if __name__ == "__main__":
  main()
