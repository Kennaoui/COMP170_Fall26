#Solution for exercise 2 from Slides (done in class)

#Pseudocode: 
#Print header line
#Loop to print the top half
#Loop to print the bottom half
#Print header line again

def complex_display_top():
    line = '#' + '=' * 16 + '#'
    print(line)
    for i in range(1, 5):
        print('|'+(-2*i+8)*' '+'<>'+'.'*(4*i-4)+ '<>'+(-2*i+8)*' '+'|')
    #Add the loop for the bottom half
    print(line)
    

complex_display_top()
