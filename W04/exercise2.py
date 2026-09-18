#Solution for exercise 2 from Slides (done in class)

#Pseudocode: 
#Print header line
#Loop to print the top half
#Loop to print the bottom half
#Print header line again

DELIMITER = '|'
DIAMOND = '<>'
SPACE = " "
LINE = '#' + '=' * 16 + '#'

def spaces(index:int) -> int:
    return -2*index + 8

def dots(index:int) -> int:
    return 4*index - 4

def resizable_spaces(line:int, size : int) -> int:
    return -2 * line + 2*size




def complex_display_top():   
    print(LINE)
    for i in range(1, 5):
        s = spaces(i)
        d = dots(i)
        print(DELIMITER +SPACE * s +DIAMOND +'.'*d+ DIAMOND+s*SPACE+ DELIMITER)

def complex_display_bottom():
    for i in range(4, 0, -1):
        s = spaces(i)
        d = dots(i)
        print(DELIMITER +SPACE * s +DIAMOND +'.'*d+ DIAMOND+s*SPACE+ DELIMITER)
    print(LINE)
    

def complex_display():
    complex_display_top()
    complex_display_bottom()

def line(size: int) -> str:
    """ """
    eq = 4 * size 
    return '#' + '=' * eq + '#'

def resizable_display_top(size : int):
    print(line(size))
    for i in range(1, size+1):
        s = resizable_spaces(i, size)
        d = dots(i)
        print(DELIMITER +SPACE * s +DIAMOND +'.'*d+ DIAMOND+s*SPACE+ DELIMITER)


resizable_display_top(10)