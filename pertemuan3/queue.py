from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
queue.append("Graham")

# print queue.popleft() akan mengetahui data mana yang akan dihapus
print(queue.popleft()) # menghapus data dari data pertama
print(queue.popleft()) # menghapus data dari data pertama
print(queue) # tampilkan data
