from timeit import Timer
result = Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()
print(result)
result = Timer('a,b = b,a', 'a=1; b=2').timeit()
print(result)
