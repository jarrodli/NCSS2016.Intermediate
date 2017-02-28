def numbers_in_numbers(x, y):
    t = 0
    for n in range(1, y+1):
        if str(x) in str(n):
            t += 1
            print(n, 'contains', x)
    print('Found', t, 'number(s) containing', x, 'between 1 and', y)

numbers_in_numbers(input("Search for:"), int((input("In range up to: "))))