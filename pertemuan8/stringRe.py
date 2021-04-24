import re
result = re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
print(result)
result = re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')
print(result)
