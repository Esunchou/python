# 生成器案列


# 移动平均数
def init(func):
    def inner(*args, **kwargs):
        ret1 = func(*args, **kwargs)
        ret1.__next__()
        return ret1
    return inner


@init
def average():
    sum1 = 0
    count = 0
    avg = 0
    while True:
        num = yield avg
        sum1 += num
        count += 1
        avg = sum1/count


avg_g = average()
ret2 = avg_g.send(10)
print(ret2)
ret3 = avg_g.send(20)
print(ret3)
ret4 = avg_g.send(30)
print(ret4)


# yield语法糖
def generator():
    a = "123456"
    b = "abcdef"
    yield from a
    yield from b


g = generator()
for i in g:
    print(i)

