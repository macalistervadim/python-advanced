

dct = {}
for i in range(10):
    dct[i] = i
    
print(dct)

print(dct.setdefault(9, 11))
print(dct)

print(dct.setdefault(11, 11))
print(dct)