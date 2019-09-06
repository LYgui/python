'''
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
'''

# 练习 使用迭代查找一个list中最小和最大值，并返回一个tuple


def findMinAndMax(L):
    if len(L) == 0:
        return (None, None)
    elif len(L) == 1:
        findmin = findmax = L[0]
        return findmin, findmax
    else:
        findmin = findmax = L[0]
        for x in L:
            if x < findmin:
                findmin = x
            if x > findmax:
                findmax = x
        return findmin, findmax


# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')


'''
print(findMinAnMax([7, 1, 3, 5, 9]))
print(findMinAnMax([7]))
print(findMinAnMax([]))
print(findMinAnMax([7, 1]))
'''