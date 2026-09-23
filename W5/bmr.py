def get_bmr_input():
    """
    Get user input for BMR calculation.
    Returns:
        weight (float): Weight in kilograms.
        height (float): Height in centimeters.
        age (int): Age in years.
        gender (str): Gender ('male' or 'female').
    """
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in centimeters: "))
    age = int(input("Enter your age in years: "))
    gender = input("Enter your gender (male/female): ").strip().lower()
    
    return weight, height, age, gender
