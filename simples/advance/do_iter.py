d = {'a': 1, 'b': 2, 'c': 3}
# 迭代key
for key in d:
    print(key)

# 迭代value
for value in d.values():
    print(value)

# 同时迭代key， value
for key, value in d.items():
    print(key, value)


from collections import Iterable
print(isinstance('abc', Iterable))
print(isinstance([1, 2, 3], Iterable))
print(isinstance(123, Iterable))
