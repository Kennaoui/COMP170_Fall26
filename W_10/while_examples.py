def years_to_reach(balance: float, goal: float, rate: float) -> int:​
    """Return years of growth until balance reaches goal."""​
    years = 0​  
    while balance < goal:​  
       balance = balance + balance * rate​ 
       years = years + 1​  
    return years​

def count_characters() -> int:​
    """Return total characters typed before quit."""​
    total = 0                       # 1 before the loop​
    entry = input("Text: ")         # 2 priming read​
    while entry != "quit":          # 3 check first​
      total = total + len(entry)  # 4 process​
      entry = input("Text: ")     # 5 read next​
    return total                    # 6 after the loop​

def total_purchases() -> float:​
    """Read amounts until -1; return their total."""​
    total = 0.0​
    amount = float(input("Amount (-1 to finish): "))​
    while amount != -1:​
       total = total + amount​
       amount = float(input("Amount (-1 to finish): "))​
    return total

def draw_fence(n:int) -> None: ​
     """ draw a fence with n sections and n + 1 posts, such as |=|=|=| for n=3"""​
     print("|", end="")  # First post ​
     for i in range(n): ​
         print("=|", end="")  # One section and its next post ​
     print()  # Move to a new line​
​
