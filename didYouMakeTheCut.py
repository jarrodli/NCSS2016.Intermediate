def did_you_make_the_cut(t):
    t == 0
    while t > 1:

        if t % 2 == 1:
            t //= 2
            t += 1
            print('Competitors:', int(t))

        else:
            t /= 2
            print('Competitors:', int(t))


did_you_make_the_cut(int(input('Total competitors: ')))