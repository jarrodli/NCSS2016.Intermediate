def double_plural(s):

    if len(s) > 0:
        words = s.split()
        j = 0
        for i in words:
            if i[-1] == 's':
                words[j] = i.replace(i,i[:-1]+i[:-1])
            j += 1
        print('\n'.join(words))
    else:
        pass

double_plural(input('Words: '))