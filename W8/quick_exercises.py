def exercise1(): 
    values = [10, 20, 30, 40, 50]
    word = "PYTHON"
    print(values[-1]) #50
    print(values[1:4]) # [20, 30, 40]
    print(word[-1]) # 'N'
    print(word[1:4]) # "YTH"
    print(len(word)) # 6
    print("TH" in word) # True
    print(values[len(values)-2:]) # [40, 50]
    print(word[-2:]) # "ON"

exercise1()

def exercise2():
    names = ["ada", "ben"]
    other = names # other = ["ada", "ben"]
    copy = names[:] # copy = ["ada", "ben"]
    other[0] = "mia" # other = ["mia", "ben"]
    copy.append("lee") # copy = ["ada", "ben","lee"]
    word = "ada" 
    word.upper() # word?

    print(names) # names = ["mia", "ben"]
    print(other) # other = ["mia", "ben"]
    print(copy)  # copy = ["ada", "ben","lee"]
    print(word)  # word = "ada"

    word = word.upper() # word = "ADA"
    word = 'I' + word[1:]    # word = "IDA"
