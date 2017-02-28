d = dict()


def password(file):
    global d
    with open(file) as file:
        for line in file:
            c = line.rstrip().split(',')
            if c[0] in d:
                d[c[0]].append(c[1])
            else:
                d[c[0]] = c[1]

    hk = max(d, key=d.get)
    print('Most common encrypted password:', hk)
    print('Password hints:\n' + len(d[hk]))


password(input('Enter filename: '))