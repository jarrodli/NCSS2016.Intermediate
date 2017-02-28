def census(x):
    d = dict()
    n = 0
    if not x:
        return None

    with open('census.txt') as file:
        for line in file:
            c = line.rstrip().split(',')
            if c[3] in d:
                d[c[3]] += c[2]
                d[c[3]] += c[4]
                n += 1
            else:
                d[c[3]] = c[2]
                d[c[3]] = c[4]
                n += 1
    print(d)

    if x in d:
        print('Statistics for', x + '.')

    else:
        print('No data found for', x + '.')
        census(input('Suburb: '))

    print('Average age:', d[x[0]] / n)
    print('Languages:', sorted(d[x[1:]]))


census(input('Suburb: '))