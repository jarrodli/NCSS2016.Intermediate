'''

attempt 1

def flavour_of_the_month(f):
    if not f:
        return None

    with open('flavours.txt', 'r') as fileinput:

        if any(f.lower() in i.lower() for i in fileinput):
            print('Done it already.')
            flavour_of_the_month(input('Check flavour: '))

        else:
            print('Sounds good!')
            flavour_of_the_month(input('Check flavour: '))

flavour_of_the_month(input('Check flavour: ')

'''

# attempt 2

flst = []


def flavour_of_the_month(f):
    global flst
    if not f:
        return None

    with open('flavours.txt', 'r') as fileinput:
        for i in fileinput:
            flst.append(i.rstrip().lower())

        if f.lower() in flst:
            print('Done it already.')
            flavour_of_the_month(input('Check flavour: '))
        else:
            print('Sounds good!')
            flavour_of_the_month(input('Check flavour: '))

flavour_of_the_month(input('Check flavour: '))

