squares = [1, 4, 9, 16, 25] # array squares
print(squares) # menampilkan array squares
print(squares[0]) # indeks 0 dari array squares
print(squares[:]) # sama seperti baris ke 2, namun menghasilkan shallow copy
cubes = [1, 8, 27, 65, 125] # hasil array nampak ada kesalahan yaitu 65
cubes[3] = 64 # ubah nilai dari indeks ke-3
print(cubes) # tampilkan
cubes.append(216)  # tambahkan pangkat 3 dari 6
cubes.append(7 ** 3) # tambahkan pangkat 3 dari 7
print(cubes) # tampilkan
print(len(cubes)) # jumlah array dari cubes
cubes[:] = [] # kosongkan list cubes
print(cubes) # hasil cubes setelah dikosongkan
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n] # nest list dari array a dan n
print(x[0]) # tampilkan hasil array a
print(x[0][1]) # tampilkan hasil array a dengan indeks ke-1 dari array n
