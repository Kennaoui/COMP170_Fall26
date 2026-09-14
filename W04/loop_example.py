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

example2()
