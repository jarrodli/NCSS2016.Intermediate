def ordinal_num(n):
    if n < 20:
        if n == 1:
            suffix = 'st'
        elif n == 2:
            suffix = 'nd'
        elif n == 3:
            suffix = 'rd'
        else:
            suffix = 'th'
    else:
        tens = str(n)
        tens = tens[-2]
        unit = str(n)
        unit = unit[-1]
        if tens == "1":
            suffix = "th"
        else:
            if unit == "1":
                suffix = 'st'
            elif unit == "2":
                suffix = 'nd'
            elif unit == "3":
                suffix = 'rd'
            else:
                suffix = 'th'
    print(str(n) + suffix)


ordinal_num(int(input("Enter a number: ")))
