# # 1.看代码写结果
# v1 = [1, 2, 3, 4, 5]
# v2 = [v1, v1, v1]
# v1.append(6)
# print(v1)
# print(v2)

# [1, 2, 3, 4, 5,6]
# [[1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6]]

# # 2.看代码写结果  代码从上至下, 修改 覆盖
# v1 = [1, 2, 3, 4, 5]
# v2 = [v1, v1, v1]
# v2[1][0] = 111
# v2[2][0] = 222
# print(v1)
# print(v2)

# v1 = [222, 2, 3, 4, 5]
v2 = [[222, 2, 3, 4, 5, 6], [222, 2, 3, 4, 5, 6], [222, 2, 3, 4, 5, 6]]   #***错题***

# # 3.看代码写结果，并解释每一步的流程。
# v1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# v2 = {}
# for item in v1:
#     if item < 6:
#         continue
#     if 'k1' in v2:
#         v2['k1'].append(item)
#     else:
#         v2['k1'] = [item]
# print(v2)
v2 = {'k1': [6, 7, 8, 9]}   #***错题***

# 4.简述深浅拷贝？
# 浅拷贝: 在内存中开辟一个新的空间存放copy的对象, 但是里面的所有元素与copy对象里面的元素共用一个内存
# 深拷贝: 在内存中开辟一个新的空间存放copy对象, 不可变得数据局类型用原来的内存, 可变的开辟新的内存

# 5.看代码写结果
# import copy
# v1 = "alex"
# v2 = copy.copy(v1)
# v3 = copy.deepcopy(v1)
# print(v1 is v2)                                     #True
# print(v1 is v3)                                     #True 字符串是不可变，所以依然用原来的内存

# 6.看代码写结果
# import copy
# v1 = [1, 2, 3, 4, 5]
# v2 = copy.copy(v1)
# v3 = copy.deepcopy(v1)
# print(v1 is v2)                                     #Flase  ***错题***
# print(v1 is v3)                                     #flase

# 7.看代码写结果
# import copy
# v1 = [1, 2, 3, 4, 5]
# v2 = copy.copy(v1)
# v3 = copy.deepcopy(v1)
# print(v1[0] is v2[0])                               #True
# print(v1[0] is v3[0])                               #True
# print(v2[0] is v3[0])                               #True

# 8.看代码写结果
# import copy
# v1 = [1, 2, 3, 4, [11, 22]]
# v2 = copy.copy(v1)
# v3 = copy.deepcopy(v1)
# print(v1[-1] is v2[-1])                             #True
# print(v1[-1] is v3[-1])                             #Flase
# print(v2[-1] is v3[-1])                             #Flase

# 9.看代码写结果
# import copy
# v1 = [1, 2, 3, {"name": '太白', "numbers": [7, 77, 88]}, 4, 5]
# v2 = copy.copy(v1)
# print(v1 is v2)                                     #Flase
# print(v1[0] is v2[0])                               #True
# print(v1[3] is v2[3])                               #True
# print(v1[3]['name'] is v2[3]['name'])               #True
# print(v1[3]['numbers'] is v2[3]['numbers'])         #True
# print(v1[3]['numbers'][1] is v2[3]['numbers'][1])   #True

# # 10.看代码写结果
# import copy
# v1 = [1, 2, 3, {"name": '太白', "numbers": [7, 77, 88]}, 4, 5]
# v2 = copy.deepcopy(v1)
# print(v1 is v2)                                     #Flase
# print(v1[0] is v2[0])                               #True
# print(v1[3] is v2[3])                               #Flase
# print(v1[3]['name'] is v2[3]['name'])               #True
# print(v1[3]['numbers'] is v2[3]['numbers'])         #Flase
# print(v1[3]['numbers'][1] is v2[3]['numbers'][1])   #True

# 11.请说出下面a, b, c三个变量的数据类型。

# a = ('太白金星')  #字符串

# b = (1,)        #元组

# c = ({'name': 'barry'}) #字典

# # 12.按照需求为列表排序：
# l1 = [1, 3, 6, 7, 9, 8, 5, 4, 2]
# # 从大到小排序
# l1.sort(reverse=True)
# print(l1)
# # 从小到大排序
# l1.sort()
# print(l1)
# # 反转l1列表
# l1.reverse()
# print(l1)

# # 13.利用python代码构建一个这样的列表(**升级题 **)：[['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
# l1 = []
# l2 = []
# for i in range(3):
#     l1.append('_')
#     l2.append(l1)
# print(l2)


# # 14.看代码写结果：
# l1 = [1, 2 ]
# l1 += [3, 4]
# print(l1)

# # 15.看代码写结果：
# dic = dict.fromkeys('abc', [])
# dic['a'].append(666)
# dic['b'].append(111)
# print(dic)

# # 16.l1 = [11, 22, 33, 44, 55]，请把索引为奇数对应的元素删除（不能一个一个删除，此l1只是举个例子，里面的元素不定）
# l1 = [11, 22, 33, 44, 55,66,77,88,99,100]
# l2 = []
# for i in l1:
#     if i % 2 == 1:
#         l1.remove(i)
# print(l1)


# # 17. dic = {'k1' : '太白', 'k2' : 'barry', 'k3' : '白白', 'age' : 18} 请将字典中所有键带k元素的键值对删除.
# dic = {'k1' : '太白', 'k2' : 'barry', 'k3' : '白白', 'age' : 18}
# for keys in list(dic.keys()):
#     if 'k' in keys:
#         dic.pop(keys)
# print(dic)

# 18.bytes数据类型是python的基础数据类型，bytes类型存在的意义是什么？

# 用于各种编码方式的转换

# 19.列举bytes类型与str类型的三个不同点？
# 在内存中编码不同;
# 英文 str'hello' bytes: b'Hello ;
# 中文 str:'中国' bytes:b'\xe4\xb8\xad\xe5\x9b\xbd'

# # 20.完成下列需求：
# s1 = '太白金星'
# # 将s1转换成utf-8的bytes类型。
# s = s1.encode('utf-8')
# print(s)
#
# # 将s1转化成gbk的bytes类型。
# s = s1.encode('gbk')
# print(s)
# # b为utf-8的bytes类型，请转换成gbk的bytes类型。
# b = b'\xe5\xa4\xaa\xe7\x99\xbd\xe6\x9c\x80\xe5\xb8\x85'
# str_utf = b.decode('utf-8')  #反编译成UTF-8的字符
# str_gbk = str_utf.encode('gbk')  #
# print(str_gbk)

# # 21.用户输入一个数字，判断一个数是否是水仙花数。 水仙花数是一个三位数, 三位数的每一位的三次方的和还等于这个数.那这个数就是一个水仙花数,
# # 例如: 153 = 1 ** 3 + 5 ** 3 + 3 ** 3
# count = input('请输入一个数字：').strip()
# sum = 0
# for i in count:
#     a = int(i)**3
#     sum += int(a)
# if sum == int(count):
#     print('是')
# else:print('不是')
# print(count)
# print(sum)

# # # 22.把列表中所有姓周的⼈的信息删掉(此题有坑, 请慎重):
# lst = ['周⽼⼆', '周星星', '麻花藤', '周扒⽪']
# new_str = []
# for i in lst:
#     if '周' not in i:
#         new_str.append(i)
# print(new_str)
# 23.车牌区域划分, 现给出以下车牌.根据车牌的信息, 分析出各省的车牌持有量.(**选做题 **)结果: {'⿊⻰江':2, '⼭东': 1, '北京': 1}
cars = ['鲁A32444', '鲁B12333', '京B8989M', '⿊C49678', '⿊C46555', '沪B25041']
locals = {'沪': '上海', '⿊': '⿊⻰江', '鲁': '⼭东', '鄂': '湖北', '湘': '湖南','京':'北京'}
# {'⿊⻰江':2, '⼭东': 1, '北京': 1}
#自己写的
# l1 = []
# l2 = []
# dic = {}
# for i in cars:
#     l1.append(i[0])
# print(l1)
# for i in l1:
#     l2.append(locals.get(i))
# print(l2)
# for i in l2:
#     dic.setdefault(i,l2.count(i))
# print(dic)

#标准答案
# dic = {}
# for i in cars:
#     if locals[i[0]] not in dic:
#         dic[locals[i[0]]] = 1
#     else:
#         dic[locals[i[0]]] += 1
# print(dic)


# 索引为奇数对应的元素删除
# l1 = [11, 22, 33, 44, 55]
# for index in range(len(l1)):
#     if index % 2 == 0:
#         l1.pop(index)
# print(l1)  #[11, 33, 44]

# del l1[1::2]
# print(l1)