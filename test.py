'''
import math
def quadratic(a, b, c):
    x=(-b+math.sqrt((b*b)-4*a*c))/(2*a)
    y=(b+math.sqrt((b*b)-4*a*c))/(2*a)
    return x,y

print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, 1.0):
    print('11')
else:
    print('22')
def findMinAndMax(L):
    a=0
    b=0
    for i,value in L:
        if value>a:
            a=value
        if b==0:
            b=value
        elif b>value:
            b=value

    return (a,b)

if findMinAndMax([7]) != (7, 7):
    print('测试失败2!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败3!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败4!')0
else:
    print('测试成功5!')

L1 = ['Hello', 'World', 18, 'Apple', None]
L2=[s.lower() for s in L1 if(isinstance(s, str))]
'''
'''
def triangel(n):
    L=[1]                                                                 #定义一个list[1]
    while True:
        yield L                                                           #打印出该list
        L=[L[x]+L[x+1] for x in range(len(L)-1)]        #计算下一行中间的值（除去两边的1）

        L.insert(0,1)                                                 #在开头插入1
        L.append(1)                                                 #在结尾添加1
        if len(L)>10:                                                 #仅输出10行
            break

#生成一个generator对象，然后通过for循环迭代输出每一行
a=triangel(10)
for i in a:
    print(i)

#利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
def normalize(s):
    return s.capitalize()

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

#接受一个list并利用reduce()求积
from functools import reduce
def prod(L):
    def fn(x, y):
        return x * y
    return reduce(fn, L)

L1 = prod([3, 5, 7, 9])
print(L1)

#回数，回数是指从左向右读和从右向左读都是一样的数
def is_palindrome(n):
    return str(n) == str(n)[::-1]

L = list(filter(is_palindrome, range(1500)))
print(L)
'''

#排序
from operator import itemgetter
students = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

print(sorted(students, key=itemgetter(0)))
print(sorted(students, key=lambda t: t[1]))
print(sorted(students, key=itemgetter(1), reverse=True))
