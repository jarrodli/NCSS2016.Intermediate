def abn_validator(n):
    lst = [int(i) for i in str(n)]
    weights = [10, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    if len(lst) == 11:
        lst[0] -= 1
        checksum = sum(a * b for a, b in zip(lst, weights)) % 89
        if checksum == 0:
            print("Valid")
        else:
            print("Invalid")
    else:
        print("Invalid")


abn_validator(input("ABN: "))
