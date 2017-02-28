def functional_hashtag(m):
    m = ''.join(m.lower().title().split())

    print('#' + m)

functional_hashtag(input('Words: '))