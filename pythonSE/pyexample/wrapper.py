# 装饰器案例
from functools import wraps
FLAG = True
FLAG2 = True


def wrapper_flag(flag):
    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            if flag:
                print("装饰1之前的操作")
                ret = func(*args, **kwargs)
                print("装饰1之后的操作")
                return ret
            else:
                ret = func(*args, **kwargs)
                return ret
        return inner
    return wrapper


def wrapper_flag2(flag):
    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            if flag:
                print("装饰2之前的操作")
                ret = func(*args, **kwargs)
                print("装饰2之后的操作")
                return ret
            else:
                ret = func(*args, **kwargs)
                return ret
        return inner
    return wrapper


@wrapper_flag(FLAG)
@wrapper_flag2(FLAG2)
def stupid():
    s = "孙大傻执行任务"
    print(s)
    return '装饰器返回完成'


n = stupid()
print(n)
print(stupid.__name__)
