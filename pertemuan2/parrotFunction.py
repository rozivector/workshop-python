def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")
parrot(1000)          # 1 posisi argument
parrot(voltage=1000)  # 1 kata kunci argument
parrot(voltage=1000000, action='VOOOOOM')   # 2 kata kunci argument
parrot(action='VOOOOOM', voltage=1000000)   # 2 kata kunci argument
parrot('a million', 'bereft of life', 'jump') # 3 posisi argument
parrot('a thousand', state='pushing up the daisies')  # 1 posisi, 1 kata kunci