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
    """Rerturn the number of spaces on each side to be added in each line 
    depending on the line we are at for size = 4.""""
    return -2*index + 8

def dots(index:int) -> int:
    """Rerturn the number of spaces on each side to be added in each line 
    depending on the line.""""
    return 4*index - 4

def complex_display_top():   
    """Display the top half of the figure for size = 4"""
    print(LINE)
    for i in range(1, 5):
        s = spaces(i)
        d = dots(i)
        print(DELIMITER +SPACE * s +DIAMOND +'.'*d+ DIAMOND+s*SPACE+ DELIMITER)

def complex_display_bottom():
    """Display the top bottom of the figure for size = 4"""
    for i in range(4, 0, -1):
        s = spaces(i)
        d = dots(i)
        print(DELIMITER +SPACE * s +DIAMOND +'.'*d+ DIAMOND+s*SPACE+ DELIMITER)
    print(LINE)
    

def complex_display():
    """Display the whole figure for size = 4"""
    complex_display_top()
    complex_display_bottom()
    
############### RESIZABLE FIGURES DISPLAY#################################################

def resizable_spaces(line:int, size : int) -> int:
    """Rerturn the number of spaces on each side to be added in each line 
    depending on the line we are at and the size of the whole figure.""""
    return -2 * line + 2*size

def line(size: int) -> str:
    """Return String that will be displayed at the top and bottom of the figure. 
    It says depends on the size. """
    eq = 4 * size 
    return '#' + '=' * eq + '#'

def resizable_display_top(size : int):
    """Display the top half of the figure for a given size"""
    print(line(size))
    for i in range(1, size+1):
        s = resizable_spaces(i, size)
        d = dots(i)
        print(DELIMITER +SPACE * s +DIAMOND +'.'*d+ DIAMOND+s*SPACE+ DELIMITER)

def resizable_display_bottom(size : int):
    """Display the bottom half of the figure for a given size"""
    pass

def resizable_display(size : int):
    """Display the bottom half of the figure for a given size"""
    pass
    
def display(): 
    """Prompt the user for a size, then display the whole figure for the given size"""
    pass

display()
