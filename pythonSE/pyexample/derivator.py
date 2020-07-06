# 各种推导式 生成器表达式

# 30以内所有被3整除的数
ret = [i for i in range(30) if i % 3 == 0]
print(ret)

# 30以内所有被3整除的数的平方
ret = [i**2 for i in range(30) if i % 3 == 0]
print(ret)

# 找到嵌套列表中名字含有两个‘e’的所有名字
names = [['Tom', 'Billy', 'Jefferson', 'Andrew', 'Wesley', 'Steven', 'Joe'],
         ['Alice', 'Jill', 'Ana', 'Wendy', 'Jennifer', 'Sherry', 'Eva']]

ret = [name for lst in names for name in lst if name.count("e") == 2]
print(ret)

# 字典推导式

# 例一：将一个字典的key和value对调
mcase = {'a': 10, 'b': 34}
# {10:'a' , 34:'b'}
mcase_frequency = {mcase[k]: k for k in mcase}
print(mcase_frequency)

# 例二：合并大小写对应的value值，将k统一成小写
mcase = {'a': 10, 'b': 34, 'A': 7, 'Z': 3}
# {'a':10+7,'b':34,'z':3}
mcase_frequency = {k.lower(): mcase.get(k.lower(), 0) + mcase.get(k.upper(), 0) for k in mcase}
print(mcase_frequency)

# 集合推导式，自带结果去重功能
# squared = {x**2 for x in [1, -1, 2]}
# print(squared)


# 各种推导式 ： 生成器 列表 字典 集合
# 遍历操作
# 筛选操作


def add(n, i):
    return n+i


def test():
    for i in range(4):
        yield i


g = test()
# for n in [1, 10, 5]:
for n in [1, 3, 4]:
    g = (add(n, i) for i in g)

# <<<0,1,2,3> + n > +n > + n>

# n = 1
# g=(add(n,i) for i in test())
# n = 10
# g=(add(n,i) for i in (add(n,i) for i in test()))
# n = 5
# g=(15,16,17,18)

print(list(g))
