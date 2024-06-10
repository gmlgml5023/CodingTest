import string
alphabet = string.ascii_lowercase
strr = input()
print(*[strr.index(a) if a in strr else -1 for a in alphabet])
