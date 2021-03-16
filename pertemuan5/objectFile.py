f = open('workfile', 'rb+')
a = f.write(b'0123456789abcdef')
print(a)
b = f.seek(5)      # Ke6 byte dalam file
print(b)
c = f.read(1)
print(c)
d = f.seek(-3, 2)  # Menuju ke 3 byte sebelum berakhir
print(d)
e = f.read(1)
print(e)
