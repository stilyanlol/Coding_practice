import re


line = input()
word = input()

pattern = fr'{word}+\b'

result = re.findall(pattern, line, flags=re.I)
print(len(result))