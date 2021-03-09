# Bilangan Fibonacci modul

def fib(n):    # buat deretan Fibonacci hingga n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):   # kembalikan bilangan deretan Fibonacci hingga n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result
    
