def get_bmr_input(user : int):
    """
    Get input from user for BMR calculation.
    Returns:
        weight (float): Weight in pounds.
        height (float): Height in inches.
        age (int): Age in years.
        gender (int): Gender (0 for 'male' or 1 for 'female').
    """
    weight = float(input("Enter weight in pounds of user #" + user + " :"))
    height = float(input("Enter height in inches of user #" + user + " :"))
    age = int(input("Enter age in years of user #" + user + " :"))
    #gender = input("Enter your gender (male/female): ").strip().lower()
    gender = int(input("Enter  0  if user #" + user + " is male, 1 otherwise:"))
    
    return weight, height, age, gender

def calculate_bmr(weight: float, height: floatt, age: int, gender: int) -> float|None:
    """
    Calculate and returns BMR for the input data: 
        weight (float): Weight in pounds.
        height (float): Height in inches.
        age (int): Age in years.
        gender (int): Gender (0 for 'male' or 1 for 'female').
    Following a gender based formula: 
        male BMR = 4.54545 x (weight in lb) + 15.875 x (height in inches) - 5 x (age in years) + 5 
        female BMR = 4.54545 x (weight in lb) + 15.875 x (height in inches) - 5 x (age in years) - 161
    if invalid Gender value: prints an error message  
    """
    if gender == 0: 
        return 4.54545 * weight + 15.875 * height - 5 * age + 5 
    elif gender == 1: 
        return 4.54545 * weight + 15.875 * height - 5 * age - 161
    else: 
        print("Invalid gender input!")

def display_user_bmr(user, bmr): 
    """
    To do:
    print a message similar to: 
        Person #2 basal metabolic rate = 1868.4
        moderate resting burn rate 
    The burn level should be determined using the table on slide 14.
    """
    pass

def main(): 
    for i in range(1,3): 
        weight, height, age, gender = get_bmr_input(i)
        bmr = calculate_bmr(weight, height, age, gender)
        display_user_bmr(i, bmr)
        


    
