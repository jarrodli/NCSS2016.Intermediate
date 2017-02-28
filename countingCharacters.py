char = []
r = 0
n = 0


def counting_characters(c):

    global char
    global n
    global r

    if len(c) > 0:
        if c in char:
            r += 1

        else:
            char.append(c)
            n += 1

        counting_characters(input('Character: '))

    else:
        print('You named', n, 'character(s). \nYou repeated', r, 'time(s).')


counting_characters(input('Character: '))