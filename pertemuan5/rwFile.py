f = open('workfile', 'w')
with open('workfile') as f:
    read_data = f.read()
x = f.closed
print(x)
