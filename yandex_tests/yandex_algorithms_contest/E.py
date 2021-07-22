from collections import Counter
a = input()
b = input()
ca = Counter(a)
cb = Counter(b)
if not (ca - cb) and len(a) == len(b):
    print(1)
else:
    print(0)