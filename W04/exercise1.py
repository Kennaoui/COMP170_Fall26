#Solution of exrcise 1 fromn slides (Live code)

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

display()
display_bigger()
