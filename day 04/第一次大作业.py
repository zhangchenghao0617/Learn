# # 1. 如何实现字符串的反转？如： name = "wupeiqi" 请反转为 name ="iqiepuw"
# name = "wupeiqi"
# name2 = name[::-1]
# print(name2)

# 2. 如何实现 “1,2,3” 变成 [‘1’,’2’,’3’]
# str ='1,2,3'
# li = []
# for i in str:
#     if i != ',':
#         li.append(i)
# print(li)
# # 3. 如何实现[‘1’,’2’,’3’]变成[1,2,3]
# li = ['1','2','3']
# li2 = []
# for i in li:
#     li2.append(int(i))
# print(li2)

# # 4. 以下代码输出是什么? list=['a','b','c','d','e'] print list[10:]
# list=['a','b','c','d','e']
# print (list[5:])
# 5.现有一列表 alist, 请写出两种去除 alist 中重复元素的方法, 其中：（**难**）
#alist=['a','b','c','a','c','a','d','e','a','c']
# # – 要求保持原有列表中元素的排列顺序。
# alist = ['a','b','c','a','c','a','d','e','a','c']
# new_list = []
# for i in alist:
#     if i not in new_list:
#         new_list.append(i)
# print(new_list)

# – 无需考虑原有列表中元素的排列顺序（**超纲**）。

#
# # 用 Python 实现 99 乘法表（**难**）
# for i in range(1,10):
#     for j in range(1,i+1):
#         print("%d*%d=%d "% (i,j,i*j),end=" ")
#     print(" ")
