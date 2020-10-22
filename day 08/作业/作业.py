''' 
# 1.有如下文件，a1.txt，分别完成以下的功能：
# ​a.将原文件全部读出来并打印。
with open('a1.txt', encoding='utf-8', mode='r')as f:
    print(f.read())

# ​b, 在原文件后面追加一行内容：信不信由你，反正我信了。
with open('a1.txt', encoding='utf-8', mode='a')as f:
    f.write('信不信由你，反正我信了。')

# c, 将原文件全部读出来，并在后面添加一行内容：信不信由你，反正我信了。
with open('a1.txt', encoding='utf-8', mode='r+')as f:
    print(f.read())
    f.write('信不信由你，反正我信了。')

# ​d, 将原文件全部清空，换成下面的内容：
# 每天坚持一点，
# 每天努力一点，
# ​每天多思考一点，
# ​慢慢你会发现，
# ​你的进步越来越大。
with open('a1.txt', encoding='utf-8', mode='w')as f:
    f.write('每天坚持一点，每天努力一点，​每天多思考一点，慢慢你会发现，​你的进步越来越大。') 
'''  # 第一题

''''
# 2.有如下文件，t1.txt,分别完成下面的功能：
# ​a, 以r的模式打开原文件，利用for循环遍历文件句柄。
with open('t1.txt', encoding='utf-8')as f:
    for line in f:
        print(line)

# b, 以r的模式打开原文件，以readlines()方法读取出来，并循环遍历readlines(), 并分析b与c有什么区别？深入理解文件句柄与readlines()结果的区别。
with open('t1.txt', encoding='utf-8')as f:
    for lines in f.readlines():
        print(lines)

# c, 以r模式读取‘葫芦娃，’前四个字符。
with open('t1.txt', encoding='utf-8') as f:
    print(f.read(4))

# ​d, 以r模式读取第一行内容，并去除此行前后的空格，制表符，换行符。
with open('t1.txt', encoding='utf-8') as f:
    print(f.readline().strip())

# ​e, 以a + 模式打开文件，先追加一行：‘老男孩教育’然后在从最开始将原内容全部读取出来。
with open('t1.txt', encoding='utf-8', mode='a+')as f:
    f.write('\n老男孩教育')
    f.seek(0)
    print(f.read())
'''  # 第二题

'''
# 3.文件a.txt内容：每一行内容分别为商品名字，价钱，个数。
# 通过代码，将其构建成这种数据类型:
# [{'name': 'apple', 'price': 10, 'amount': 3}, {'name': 'tesla', 'price': 1000000, 'amount': 1}......]并计算出总价钱。
l1 = []
count = 0
with open('a.txt', encoding='utf-8', mode='r')as f:
    for line in f:
        dic = {}
        a, b, c = line.strip().split()
        count += int(b) * int(c)
        dic['name'] = a
        dic['price'] = b
        dic['amount'] = c
        l1.append(dic)
print(l1)
print(count)
'''  # 第三题

'''
# 4.有如下文件：alex的自述，将文件中所有的alex都替换成大写的SB（文件的改的操作）。
import os
with open('alex的自述', encoding='utf-8')as f_r,\
    open('alex的自述.bak',encoding='utf-8', mode='w')as f_w:
    f_w.write(f_r.read().replace('alex','SB'))
os.remove('alex的自述')
os.rename('alex的自述.bak','alex的自述')
'''  # 第四题





# 5.文件a2.txt内容(**选做题 **)通过代码，将其构建成这种数据类型：​
# ​[{'name': 'apple', 'price': 10, 'amount': 3, year: 2012},​{'name': 'tesla', 'price': 1000000, 'amount': 1}......]
# 并计算出总价钱。
# line.strip().split(':') =
# ['name', ' apple']
# ['price', ' 10']
# ['amount', ' 3']
# ['year', ' 2012']
# ['name', ' tesla']
# ['price', ' 100000']
# ['amount', ' 1']
# ['year', ' 2013']
dic = {}
dic2 = {}
li = []
with open('a2.txt', encoding='utf-8')as f:
    for line in f:
        keys, values = line.strip().split(':')
        for i in line.strip():
            if keys not in dic:
                dic[keys] = values
            elif keys in dic:
                dic2[keys] = values
    li.append(dic)
    li.append(dic2)
print(li)

# list1_line = ['name','price','amount','year']
# with open('a2.txt', encoding='utf-8')as f:
#     lines = f.readlines()
#     dic = {}
#     for line in lines[:len(list1_line)]:
#         line = line.strip().split(":")
#         dic.setdefault(line[0],line[1])
# print(dic)

# 6.文件a3.txt内容(**选做题 **)通过代码，将其构建成这种数据类型：
# [{'序号': '1', '部门': Python, '人数': 30, '平均年龄': 26, '备注': '单身狗'},......]
