import math
a = float(input('please enter a:'))

b = float(input('please enter b:'))

c = float(input('please enter c:'))


def quadratic(a, b, c):

    if b**2-4*a*c <= 0 or a == 0:

        print('wrong')

    else:

        qq = math.sqrt(b**2-4*a*c)

        x1 = float((-b+qq)/(2*a))

        x2 = float((-b-qq)/(2*a))

        return x1, x2


print(quadratic(a, b, c))

print('quadratic(2,3,1)=', quadratic(2, 3, 1))

print('quadratic(1,3,-4)=', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):

    print('测试失败')

elif quadratic(1, 3, -4) != (1.0, -4.0):

    print('测试失败')

else:

    print('测试成功')
