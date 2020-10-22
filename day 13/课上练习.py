# func = lambda a: (a[0], a[2])
# print(func('asdfasdf'))
#
# func1 = lambda a, b: a if a > b else b
# print(func1(8, 9))

# #求字典值最小的键值对的值
# dic = {'a': 3, 'b': 2, 'c': 1}
# print(dic[min(dic, key=lambda args: dic[args])])

#返回最小年龄的人名
# l1 = [('太白', 18), ('alex', 73), ('wusir', 35), ('口天吴', 41)]
#
# print(min(l1,key=lambda args:args[1]))

def one():
    print(1)
    def two():
        return print(2)