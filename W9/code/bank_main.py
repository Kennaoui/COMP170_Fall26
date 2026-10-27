from bank_account import *

#Client Program

def main() -> None:
    """Open two accounts and show them."""

    ada: BankAccount = BankAccount("Ada", 100.0)
   
  
    ada.deposit(50.0)
    ada.withdraw(20)
    print(ada)
    print(bo)
    print(ada == bo)
    


if __name__ == "__main__":
  main()
