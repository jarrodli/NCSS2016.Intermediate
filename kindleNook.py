from shlex import split


def nook(z):

    print(" ".join("nook" if x == "kindle" else x for x in split(z)))

nook(input("Line: "))