v = {}


def make_your_vote_count():
    global v
    for i in open('votes.txt'):
        i.rstrip()
        if i not in v:
            v[i] = 1
        else:
            v[i] += 1

    for i in v:
        print(i, ":", v[i])


make_your_vote_count()
