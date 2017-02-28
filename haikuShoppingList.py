def haiku_shopping_list():
    with open('shopping.txt', 'r') as shopping:
        with open('syllables.txt', 'r') as syllables:
            lines = [line.rstrip('\n') for line in open('filename')]
            for i in lines:
                if i in syllables and syllables[-1] == 5:
                    print(i)
                    break
            for i in lines:
                if i in syllables and syllables[-1] == 7:
                    print(i)
                    break
            for i in lines:
                if i in syllables and syllables[-1] == 5:
                    print(i)
                    break

haiku_shopping_list()