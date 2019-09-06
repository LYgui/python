# 列表生成式
print(list(range(1, 11)))


# 生成[1x1, 2x2, 3x3, ..., 10x10]
L = []
for x in range(1, 11):
    L.append(x * x)
print(L)


print([x * x for x in range(1, 11) if x % 3 == 0])


print([m + n + k for m in '123' for n in '456' for k in '789'])


import os
print([d for d in os.listdir('.')])


L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [x.lower() for x in L1 if isinstance(x, str) == True]
# 测试:
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')