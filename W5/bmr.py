def get_bmr_input(i : int):
    """
    Get input from user number i for BMR calculation.
    Returns:
        weight (float): Weight in pounds.
        height (float): Height in inches.
        age (int): Age in years.
        gender (int): Gender (0 for 'male' or 1 for 'female').
    """
    weight = float(input("Enter weight in pounds of user #" + i + " :"))
    height = float(input("Enter height in inches of user #" + i + " :"))
    age = int(input("Enter age in years of user #" + i + " :"))
    #gender = input("Enter your gender (male/female): ").strip().lower()
    gender = int(input("Enter  0  if user #" + i + " is male, 1 otherwise:"))
    
    return weight, height, age, gender
