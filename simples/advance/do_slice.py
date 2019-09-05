# -*- coding: utf-8 -*-
'''
# 切片工具
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print(L[:3])  # 提取 L 的前三个元素
print(L[-2:-1])  # 提取 L 的倒数第二个元素
'''


'''
L = list(range(100))  # 创建一个0-99的实例
print(L[:10])
print(L[11:41:2])  # 每隔两个取一个
print(L[-10:-1])  # 等价于L[-10:-1]
'''


# 练习
def trim(s):
    while s[:1] == ' ':
        s = s[1:]
    while s[-1:] == ' ':
        s = s[:-1]
    return s


if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')
