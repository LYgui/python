r'''
# 定义一个函数
import math


def my_abs(x):
    if x >= 0:
        return x  # 返回原来数值
    else:
        return -x  # 返回绝对值


print(my_abs(88))  # 调用并且打印该函数


# 定义一个空函数
def nop():
    pass  # 占位符，可以让代码先跳过本函数


# 修改绝对值函数
def my_abs2(x):
    if not isinstance(x, (int, float)):  # 参数检查
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

'''
# 练习
a = float(input('input a :'))
b = float(input('input b :'))
c = float(input('input c :'))


def quadratic(a, b, c):

    if (b**2-4*a*c < 0):
        print('wrong')
    else:
        s = math.sqrt(b**2-4*a*c)
        x1 = float((-b+a*a)/(2*a))
        x2 = float((-b-a*a)/(2*a))
        return x1, x2


print(quadratic(2, 3, 1))
print(quadratic(1, 3, -4))
