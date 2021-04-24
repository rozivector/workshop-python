import random
result = random.choice(['apple', 'pear', 'banana'])
print(result)
result = random.sample(range(100), 10)   # uji coba tanpa pergantian
print(result)
print(random.random()) # random float
print(random.randrange(6)) # random integer
