lst = []


def olympic_ordering(c):

    global lst

    if len(c) >= 1:
        if c in lst:
            print("The list already contains that country.")

        else:
            lst.append(c)

        olympic_ordering(input('Country: '))

    else:

        if len(lst) != 0:
            lst.sort()
            print('Grecia\n' + '\n'.join(lst) + '\n' + 'Time Olimpico de Refugiados\nBrasil')

        else:
            print('Grecia\nTime Olimpico de Refugiados\nBrasil')

olympic_ordering(input('Country: '))
