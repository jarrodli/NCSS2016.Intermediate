def japanese_honorifics(x, y, z):
    if x in z:
        print(z.replace(x, x + "-" + y))


japanese_honorifics(input("Name: "), input("Honorific: "), input("Text: "))