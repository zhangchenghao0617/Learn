# f1 = open('D:\\1.txt',encoding='utf-8',mode='r')
# content = f1.read()
# print(content)
# f1.close()
# 1.文件的读
# 全部读
# f1 = open('文件的读',encoding='utf-8',mode='r')
# content = f1.read()
# print((content))
# f1.close()
# n个字符读
# f1 = open('文件的读',encoding='utf-8',mode='r')
# content = f1.read(5)
# print(content)
# f1.close()

# readline() 一行一行的读
# f1 = open('文件的读',encoding='utf-8',mode='r')
# print(f1.readline())
# print(f1.readline())
# print(f1.readline())
# f1.close()

# readlines() 返回一个列表,列表的每个元素即每行的内容
# f1 = open('文件的读',encoding='utf-8',mode='r')
# print(f1.readlines())
# f1.close()

# for 循环读
# f = open('文件的读', encoding='utf-8', mode='r')
# for line in f:
#     print(line)
# f1.close()

# rb模式读取 字节读
# f = open('美女.jpg', mode='rb')
# for line in f:
#     print(line)
# f.close()

# 2.文件的写
# 没有文件，创建文件，写入内容
# f = open('文件的写',encoding='utf-8',mode='w')
# f.write('试一下')
# f.close()

# 如果文件存在，先清空原文件内容，在写入新内容
# f = open('文件的写',encoding='utf-8',mode='w')
# f.write('替换掉内容')
# f.close()

# # 字节写
# f = open('美女.jpg',mode='rb')
# content = f.read()
# f.close()
# f_w = open('美女2.jpg',mode='wb')
# f_w.write(content)
# f_w.close()

# # 3.追加写
# # 没有文件创建文件，追加内容
# f = open('文件的追加', encoding='utf', mode='a')
# f.write('创建文件,写进去')
# f.close()
# # 有文件，在原文件的最后面追加内容。
# f = open('文件的追加', encoding='utf-8', mode='a')
# f.write('我爱你')
# f.close()
# 4.文件操作的其他模式 r+
# 读并追加,# 顺序不能错,先读再追加,如果是先追加,就会按光标替换第一个光标位置的内容
# f = open('文件的读并追加', encoding='utf-8', mode='r+')
# print(f.read())
# f.write('随便加点')
# f.close()

# #错误的实例,先写后读
# f = open('文件的读并追加', encoding='utf-8', mode='r+')
# f.write('加加加')
# print(f.read())
# f.close()
# #把前面的三个字符替换掉了

# # 5.文件的其他操作方法
# # tell() 获取光标的位置,单位是字节
# f = open('文件的其他操作方法', encoding='utf-8', mode='r')
# print(f.tell())
# f.read()
# print(f.tell())
# f.close()

# # seek()调整光标的位置
# f = open('文件的其他操作方法', encoding='utf-8', mode='r')
# f.seek(6)  # 因为UTF-8编码,一个汉字三个字节,所以必须是3的倍数,不然就会报错
# print(f.read())
# f.close()

# # flush() 强制刷新,用于文件未关闭保存的硬盘前,强制刷新到硬盘中，同时清空缓冲区。
# f = open('文件的其他操作方法', encoding='utf-8', mode='w')
# f.write('文件的强制刷新')
# f.flush()
# f.close()

# # 6.文件的另外一种打开方式  '优点:1.不用关闭文件句柄/n 2.可以打开多个文件'  缺点：待续
# with open('文件的读', encoding='utf-8', mode='r') as f,\
#         open('文件的另一种打开方式', encoding='utf-8', mode='w') as f_r:
#     print(f.read())
#     f_r.write('缺点：暂时不讲')

'''
1, 以读的模式打开原文件。
2，以写的模式创建一个新文件。
3，将原文件的内容读出来修改成新内容，写入新文件。
4，将原文件删除。
5，将新文件重命名成原文件。
'''
# import os
# with open('文件的改', encoding='utf-8', mode='r') as f_r,\
#         open('文件的改.bak', encoding='utf-8', mode='w') as f_w:
#     old_content = f_r.read()  # 1, 以读的模式打开原文件。
#     new_content = old_content.replace('alex', '太白')  # 2,将原文件的内容读出来修改成新内容
#     f_w.write(new_content)   # 3,写入新文件
# os.remove('文件的改')  # 4,将原文件删除。
# os.rename('文件的改.bak', '文件的改')   # 5,将新文件重命名成原文件。

# # 改进版
# import os
# with open('文件的改', encoding='utf-8', mode= 'r') as f_r,\
#         open('文件的改.bak', encoding= 'utf-8', mode='w') as f_w:
#     for line in f_r:
#         new_line = line.replace('太白','alex')
#         f_w.write(new_line)
# os.remove('文件的改')
# os.rename('文件的改.bak','文件的改')

