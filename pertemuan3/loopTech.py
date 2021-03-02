knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items(): # untuk mencocokan value dengan key
    print(k, v)
for i, v in enumerate(['tic', 'tac', 'toe']): # mencocokan posisi index dengan key
    print(i, v)
# untuk loop lebih dari 2 urutan yang sama gunakan zip()
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))
# untuk urutan terbalik gunakan reversed()
for i in reversed(range(1, 10, 2)):
    print(i)
# untuk urutan yang diurutkan gunakan sorted()
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for i in sorted(basket):
    print(i)
# untuk eliminasi duplikat urutan gunakan set()
for f in sorted(set(basket)):
    print(f)
