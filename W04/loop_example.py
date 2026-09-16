def example1():
    high_temp = 5
    for i in range(-3, high_temp // 2 + 1):
        print(i * 1.8 + 32) # here we need the counter i
        high_temp = 3

def example2():
    """print this message: T-minus 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, blastoff! 
    The end."""

    print("T-minus", end=' ')
    for i in range(10, 0, -1):
        print(i, end=', ')
    print("blastof!\nThe end.")

def example3():
    """print this shape: 
    +----+
    \\    /
    /    \\
    \\    /
    /    \\
    \\    /
    /    \\
    +----+ 
    """ 
    print("+----+") # this is printed before the for loop
    for i in range(3): # Or range(1,4)
        print("\\    /")
        print("/    \\")
    print("+----+") # this is printed after the for loop 


def display():
    line = "+" + '/\\' * 4 + '+'
    print(line)
    for _ in range(2):
        print('|' + ' '* 8 + '|')
    print(line)

def display_bigger():
    line = "+" + '/\\' * 10 + '+'
    print(line)
    for _ in range(5):
        print('|' + ' '* 20 + '|')
    print(line)

def complex_display_top():
    line = '#' + '=' * 16 + '#'
    print(line)
    for i in range(1, 5):
        print('|'+(-2*i+8)*' '+'<>'+'.'*(4*i-4)+ '<>'+(-2*i+8)*' '+'|')
    #Add the loop for the bottom half
    print(line)
    

complex_display_top()
