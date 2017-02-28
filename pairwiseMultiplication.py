def pairwise_multiply(x, y):
    print([a*b for a, b in zip(x, y)])

pairwise_multiply(input('Enter two lists: '))