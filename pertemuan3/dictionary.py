tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print(tel)
print(tel['jack'])
del tel['sape']
tel['irv'] = 4127
print(tel) # dictionary sederhana
print(list(tel)) # tampilkan daftar kata
print(sorted(tel)) # urutkan
print('guido' in tel) # apakah ada di daftar tel?
print('jack' not in tel) # bukan di daftar tel?
# konstruktor dictionary
words = dict(sape=4139, guido=4127, jack=4039) # dengan key value non string
print(words) # lebih sederhana