contents = {}


def kitchen_contents(c):

    global contents

    if not c:
            return None

    c = c.split()

    if c[0].lower() == 'set' and len(c) > 2:
        i = c[1]
        v = c[2]
        contents[i] = int(v)
        kitchen_contents(input('Command: '))

    elif c[0].lower() == 'query' and c[1] in contents:
        print('You have', contents.get(c[1]), c[1] + '.')
        kitchen_contents(input('Command: '))

    elif c[1] not in contents and c[0] == 'query':
        print('I have no information about', c[1] + '.')

    else:
        print('Unknown command!')
        kitchen_contents(input('Command: '))


kitchen_contents(input('Command: '))