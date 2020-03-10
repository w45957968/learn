# -*- coding: utf-8 -*-

# 完数——一个数的因数之和 恰好等与其自身的数

def max(num):
    list = set()
    for i in range(1, num):
        if num % i == 0:
            list.add(i)

    sum = 0
    for i in list:
        sum += i

    if sum == num:
        print(list)
        print(num)


for i in range(1, 10001):
    max(i)
