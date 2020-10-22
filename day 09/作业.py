# 1.整理函数相关知识点,写博客。
# #2.写函数，检查获取传入列表或元组对象的所有奇数位索引对应的元素，并将其作为新列表返回给调用者。
# def qishu(content):
#     return content[::2]
# print(qishu((1,2,3,4,5,6,7,8,9,10)))

# #3.写函数，判断用户传入的对象（字符串、列表、元组）长度是否大于5。
# def panduan(a):
#     a = '大于' if len(a)>5 else '小于'
#     return a
# print(panduan([1,2,3,4,5,6,7,8,9,10]))

# # 4.写函数，检查传入列表的长度，如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
# def jiancha(a):
#     return a[:2] if len(a) > 2 else a
# print(jiancha([1,2,3,4,5,6,7,8,9,10]))

# # 5.写函数，计算传入函数的字符串中,[数字]、[字母] 以及 [其他]的个数，并返回结果。
# def count(a):
#     shuzi = 0
#     zimu = 0
#     qita = 0
#     for i in a:
#         if i.isdecimal():
#             shuzi += 1
#         elif i.isalpha():
#             zimu += 1
#         else:
#             qita += 1
#     return shuzi,zimu,qita
# print(count('11asdf489asd21f8af%$%'))
#
# # 6.写函数，接收两个数字参数，返回比较大的那个数字。
# def bijiao(a,b):
#     return a if a > b else b
# print(bijiao(3,4))

# # 7.写函数，检查传入字典的每一个value的长度,如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
# dic = {"k1": "v1v1", "k2": [11,22,33,44]}
# def new_value(dic):
#     li  = []
#     for i in dic.values():
#         li.append(i[:2])
#     return li
# print(new_value(dic))
#
# n = []
# def func(dic):
#     for i in dic:
#         if len(dic[i])>2:
#             n.append(dic[i][:2])
#     return n
# print(func(dic= {"k1": "v1v1", "k2": [11,22,33,44]}))
#
# def func(dic):
#     for key,value in dic.items():
#         if len(value)>2:
#             value = value[0:2]
#         dic[key] = value
#     return dic
# print(func(dic= {"k1": "v1v1", "k2": [11,22,33,44]}))

#
#
# # 8.写函数，此函数只接收一个参数且此参数必须是列表数据类型，此函数完成的功能是返回给调用者一个字典，此字典的键值对为此列表的索引及对应的元素。例如传入的列表为：[11,22,33] 返回的字典为 {0:11,1:22,2:33}。
# def dic(a):
#     dic= {}
#     for i in range(len(a)):
#         dic[i] = a[i]
#     return dic
# print(dic([11,22,33]))

# # 9.写函数，函数接收四个参数分别是：姓名，性别，年龄，学历。用户通过输入这四个内容，然后将这四个内容传入到函数中，此函数接收到这四个内容，将内容追加到一个student_msg文件中。
# def func(name,sex,age,education):
#     with open('student_msg.txt', encoding='utf-8', mode='w')as f:
#             content = name+sex+age+education
#             f.write(content)
#             return '写入'
# func('张三','nan','18','daxue')
# name = input('请输入姓名：')
# sex = input('请输入性别：')
# age = input('请输入年龄：')
# education = input('请输入学历：')
# func(name, sex, age, education)

# # 10.对第9题升级：支持用户持续输入，Q或者q退出，性别默认为男，如果遇到女学生，则把性别输入女。
# def func(name,age,education,sex = '女',):
#     with open('student_msg.txt', encoding='utf-8', mode='a')as f:
#             content = "姓名:%s,性别:%s,年龄:%s,学历:%s\n" %(name,sex,age,education)
#             f.write('\n'+content)
#             return '写入'
# while 1:
#     print('请输入新的数据')
#     name = input('请输入姓名：')
#     if name.upper() == 'Q':
#         break
#     sex = input('请输入性别：')
#     if sex.upper() == 'Q':
#         break
#     age = input('请输入年龄：')
#     if age.upper() == 'Q':
#         break
#     education = input('请输入学历：')
#     if education.upper() == 'Q':
#         break
#     func(name,age, education,sex)

# #11、写函数，用户传入修改的文件名，与要修改的内容，执行函数，完成整个文件的批量修改操作（选做题）。
# import os
# def wenjian(path,old_content,new_content):
#     with open(path, encoding='utf-8', mode='r')as f_r,\
#             open(path+'.bak', encoding='utf-8', mode='w') as f_w:
#             for line in f_r:
#                 new = line.replace(old_content,new_content)
#                 f_w.write(new)
#     os.remove(path)
#     os.rename(path+'.bak',path)
# wenjian('春天的一段话','123','卧春')