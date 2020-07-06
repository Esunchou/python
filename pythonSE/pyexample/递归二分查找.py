# 二分查找算法 必须处理有序的列表
list1 = [2, 3, 5, 10, 15, 16, 18, 22, 26, 30, 32, 35, 41, 42, 43, 55, 56, 66, 67, 69, 72, 76, 82, 83, 88]


def find(l, aim, start=None, end=None):
    start = start if start else 0
    end = end if end else len(l) - 1
    mid_index = (end - start)//2 + start
    if start <= end:
        if l[mid_index] < aim:
            return find(l, aim, start=mid_index + 1, end=end)
        elif l[mid_index] > aim:
            return find(l, aim, start=start, end=mid_index - 1)
        else:
            return mid_index
    else:
        return '找不到这个值'


print(find(list1, 88))


# 斐波那契  # 问第n个斐波那契数是多少
# 在一个函数中，不要使用双递归，否则导致大量重复计算
# def fib(n,l = [0]):
#     l[0] +=1
#     if n ==1 or n == 2:
#         l[0] -= 1
#         return 1,1
#     else:
#         a,b = fib(n-1)
#         l[0] -= 1
#         if l[0] == 0:
#             return a+b
#         return b,a+b
# print(fib(1))

# def fib(n, k = 0):
#     a,b = 0,0
#     k += 1
#     if n == 1 or n == 2:
#         k -= 1
#         a,b = 1,1
#     else
#         k
#         a,b = fib(n-1)


