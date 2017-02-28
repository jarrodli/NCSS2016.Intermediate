def rally_navigator(x):
    lst = [str(i) for i in x]
    f = []
    while len(f) < len(lst):
        for i in lst:
            if i == 'r':
                f.append('right')
            elif i == 'l':
                f.append('left')
            elif i == 'j':
                f.append('jump')
            elif i == 's':
                f.append('straight')
            else:
                f.append('Aaaaah!')
    if len(f) > 0:
        print("\n".join(f))

    else:
        pass


rally_navigator(input('Terrain: '))
