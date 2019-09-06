'''
# 列表列表生成式
L = [x * x for x in range(1, 11)]
print(L)

# 生成器
L1 = (x * x for x in range(1, 11))
for x in L1: # 通过for循环打印生成器
	print(x)



# 斐波拉契数列
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        # print(b)
        yield b  # 改成生成器,如果一个函数定义中包含yield关键字,那么这个函数就不再是一个普通函数，而是一个generator
        a, b = b, a + b
        n = n + 1
    return 'done'


for x in fib(10):  # 用for循环调用generator时，发现拿不到generator的return语句的返回值
    print(x)
'''


# 练习
def triangles():
    L = [1]
    while True:
        yield L
        L = [0] + L + [0]
        L = [L[i] + L[i + 1] for i in range(len(L) - 1)]


# 期待输出:
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
n = 0
results = []
for t in triangles():
    results.append(t)
    n = n + 1
    if n == 10:
        break

for t in results:
    print(t)

if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')
