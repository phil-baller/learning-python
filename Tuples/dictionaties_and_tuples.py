"""d = {'z': 1, 'c': 3, 'a': 5}
t = list(d.items())
t.sort()
print(t)"""

d = {'a': 10, 'b': 1, 'c': 22}
for key, val in list(d.items()):
    print(val, key)