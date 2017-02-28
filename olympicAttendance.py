def olympic_attendance(n):

    x = 0
    d = {}
    while x < n:
        with open('day' + str(n - x) + '.txt') as f:
            for line in f:
                c = line.rstrip().split(',')
                if c[0] in d:
                    d[c[0]] += int(c[1])
                else:
                    d[c[0]] = int(c[1])
        x += 1
    y = sum(d.values())
    for i in d:
        print(i + ':', d[i])

    print('In total:', str(y), 'attendees.')

olympic_attendance(int(input('How many days of records do you have? ')))






