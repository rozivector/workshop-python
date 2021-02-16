print('Ini String') # string petik tunggal
print("Ini String") # string petik dua
print("Al \'Arabic") # kutip string dengan karakter petik didalamnya
print("Pertama \nKedua") # baris baru
print(r"Output: C:\File\nama") # menghindari kesalahan penulisan format dengan menambahkan r sebelum tanda petik
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""") # String dengan baris ganda
print(3 * 'ke' + 'rabat') # dapat menulis string sebanyak perkalian n
print('py' 'thon') # String dapat dipisahkan namun hasil akan digabungkan

prefix = 'py' # inisialisasi variabel
print(prefix + 'thon') # diperlukan operand + untuk menghasilkan sebuah string dari variabel
word = 'python'
print(word[0]) # indeks string dengan posisi awal 0
print(word[0:2]) # indeks string dengan posisi 0 dan pengecualian atau berakhir di 2
print(word[-1]) # indeks string kebalikan menjadi posisinya di akhir indeks
print(word[2:]) # indeks string dimulai dari posisi ke-2 sampai akhir
print(len(word)) # ukuran string
