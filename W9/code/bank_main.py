from bank_account import *

#Client Program

def main() -> None:
    """Open two accounts and show them."""

    ada = BankAccount("Ada", 100.0)
    bo = BankAccount("Bo")
  
    print(ada.owner, ada.balance)
    print(bo.owner, bo.balance)

    bo.deposit(50.0)
    print(bo.get_balance())

    if ada.can_afford(150):
        print("you can afford!")
    


if __name__ == "__main__":
  main()
