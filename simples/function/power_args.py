'''
# 计算乘积

def power(x):
    return x * x

print(power(15))
print(power(5))
'''


'''
# 计算X的n次方

def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x  # 类似递归
    return s


print(power(4, 6)) #正常情况
print(power(5, 4)) #正常情况
print(power(5))    #调用默认参数n=2 计算平方
'''

'''
# 小学生注册

def enroll(name, gender, age=18, city='beijing'):  # 设定默认的参数。注意：定义默认参数要牢记一点：默认参数必须指向不变对象！
    print('name:', name)
    print('gender', gender)
    print('age', age)
    print('city', city)


print(enroll('YXG', 'A'))
'''


'''
# 计算a2 + b2 + c2 + ……

def calc(*numbers):  # 加一个 * 把参数设定为可变参数，允许传入0个或者任意个参数
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

nums = [1, 2, 3]
print(calc(*nums))
'''


# 关键字参数
def person(name, age, **kw):  # 关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dic,可以扩展函数的功能
	if 'city' in kw:
		# 有city资源
		pass
	if 'job' in kw:
		# 有job资源
		pass
    print('name:', name, 'age:', age, 'other:', kw)


# neme: bob age: 45 other: {'gender': 'M', 'job': 'engineer'}
print(person('bob', 45, gender='M', job='engineer'))

extra = {'city': 'beijing', 'job': 'engineer'}
# **extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra
print(person('jack', 24, **extra))
