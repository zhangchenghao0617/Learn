# # 1、请将列表中的每个元素通过"_"链接起来。['李少奇', '李启航', '渣渣辉']
# l1 = ['李少奇', '李启航', '渣渣辉']
# li = '_'.join(l1)
# print(li)
# 2.
# 请将列表中的每个元素通过"_"链接起来。['李少奇', '李启航', 666, '渣渣辉']

# # 链接起来。['李少奇', '李启航', 666, '渣渣辉']
# l2 = ['李少奇', '李启航', 666, '渣渣辉']
# # 方法一
# l2[2] = str(l2[2])
# li = '_'.join(l2)
# print(li)
# # 方法二
# list_str = []
# for i in l2:
#     list_str.append(str(i))
# li = '_'.join(list_str)
# print(li)
# # 3.请将元组v1 = (11, 22, 33)中的所有元素追加到列表v2 = [44, 55, 66]中。
# v1 = (11, 22, 33)
# v2 = [44, 55, 66]
# for i in v1:
#     v2.append(i)
# print(v2)
# # 4.请将元组v1 = (11, 22, 33, 44, 55, 66, 77, 88, 99)中的所有偶数索引位置的元素追加到列表v2 = [44, 55, 66]中。
# v1 = (11, 22, 33, 44, 55, 66, 77, 88, 99)
# v2 = [44, 55, 66]
# count = 0
# for i in v1:
#     if count % 2 == 0:
#         v2.append(i)
#     count += 1
# print(v2)


# # 5.将字典的键和值分别追加到key_list和value_list两个列表中，如：
# key_list = []
# value_list = []
# info = {'k1':'v1','k2':'v2','k3':'v3'}
# # 方法一：
# for i in info.keys():
#     key_list.append(i)
# print(key_list)
# for i in info.values():
#     value_list.append(i)
# print(value_list)
# # 方法二：
# key_list = list(info.keys())
# value_list = list(info.values())
# print(key_list)
# print(value_list)
# 6.
# 字典dic = {'k1': "v1", "k2": "v2", "k3": [11, 22, 33]}
dic = {'k1': "v1", "k2": "v2", "k3": [11, 22, 33]}
# a.请循环输出所有的key
# for i in dic.keys():
#     print(i)
# # b.请循环输出所有的value#
# for i in dic.values():
#     print(i)
# # c.请循环输出所有的key和value
# for i in dic.items():
#     print(i)
# # d. 请在字典中添加一个键值对，"k4": "v4"，输出添加后的字典
# dic.setdefault("k4","v4")
# print(dic)
# # e.请在修改字典中 "k1" 对应的值为 "alex"，输出修改后的字典
# dic['k1'] = "alex"
# print(dic)
# # f.请在k3对应的值中追加一个元素 44，输出修改后的字典
# dic['k3'].append('44')
# print(dic)
# # g.请在k3对应的值的第 1 个位置插入个元素 18，输出修改后的字典
# dic['k3'].insert(0,18)
# print(dic)

# # 7.
av_catalog = {
    "欧美": {
        "www.太白.com": ["很多免费的,世界最大的","质量一般"],
        "www.alex.com": ["很多免费的,也很大","质量挺好"],
        "oldboy.com": ["多是自拍,高质量图片很多","资源不多,更新慢"],
        "hao222.com": ["质量很高,真的很高","全部收费,屌丝请绕过"]
    },
    "日韩": {
        "tokyo-hot": ["质量怎样不清楚,个人已经不喜欢日韩范了","verygood"]
    },
    "大陆": {
        "1024": ["全部免费,真好,好人一生平安","服务器在国外,慢"]
    }
}
# # # 1.给此["很多免费的,世界最大的", "质量一般"]列表第二个位置插入一个 元素：'量很大'。
# av_catalog['欧美']["www.太白.com"].insert(1,'量很大')
# print(av_catalog)

# # # 2.将此["质量很高,真的很高", "全部收费,屌丝请绕过"]列表的"全部收费,屌丝请绕过"删除。
# av_catalog["欧美"]['hao222.com'].pop(1)
# print(av_catalog)

# #3.将此["质量怎样不清楚,个人已经不喜欢日韩范了", "verygood"]列表的"verygood"全部变成大写。
# av_catalog["日韩"]["tokyo-hot"][1] = av_catalog["日韩"]["tokyo-hot"][1].upper()
# print(av_catalog)
#
# # 4.给'大陆'对应的字典添加一个键值对'1048': ['一天就封了']
# av_catalog["大陆"].setdefault('1048',['一天就封了'])
# print(av_catalog)

# # 5.删除这个键值对："oldboy.com": ["多是自拍,高质量图片很多", "资源不多,更新慢"]
# pop = av_catalog["欧美"].pop("oldboy.com",'没有此键')
# print(pop)
# print(av_catalog)
# # 6. 给此["全部免费,真好,好人一生平安", "服务器在国外,慢"]列表的第一个元素，加上一句话：'可以爬下来'
# av_catalog.get("大陆").get("1024").insert(0,'可以爬下来')
# print(av_catalog)

# 7.有字符串"k: 1|k1:2|k2:3 |k3 :4"处理成字典{'k': 1, 'k1': 2....}


# #方法一：推荐
# str = "k: 1|k1:2|k2:3 |k3 :4"
# dic = {}
# list = str.split("|")
# # print(list)
# for i in list:
#     # print(i)
#     keys,values = i.split(":")
#     dic.setdefault(keys.strip(),int(values.strip()))
# print(dic)

# # 方法二
# str = "k: 1|k1:2|k2:3 |k3 :4"
# list = str.split("|")
# count=0 #计数器
# dic = {}
# for i in list:
#     l1 = i.split(':')
#     for j in l1:
#         j = j.strip()
#         count += 1
#         if count % 2 == 0:
#             dic.setdefault(key,int(j))
#         key = j
# print(dic)
# 8.
# 有如下值
# # li = [11, 22, 33, 44, 55, 66, 77, 88, 99, 90], 将所有大于66的值保存至字典的第一个key对应的列表中，将小于66的值保存至第二个key对应的列表中。
# li = [11, 22, 33, 44, 55, 66, 77, 88, 99, 90]
# result = {'k1': [], 'k2': []}
# for i in li:
#     if i > 66:
#         result['k1'].append(i)
#     elif i < 66:
#         result['k2'].append(i)
# print(result)

# 9.
# 输出商品列表，用户输入序号，显示用户选中的商品
# """
# 商品列表：
# goods = [
#         {"name": "电脑", "price": 1999},
#         {"name": "鼠标", "price": 10},
#         {"name": "游艇", "price": 20},
#         {"name": "美女", "price": 998}
#         ]
# # 要求:
# # 1：页面显示 序号 + 商品名称 + 商品价格，如：
# #       1 电脑 1999
# #       2 鼠标 10
# #       ...
# dic = {}
# count = 1
# for i in goods:
#     print(str(count)+" " +i["name"] +" "+ str(i["price"]))
#     dic.setdefault(str(count),i["name"] +" "+ str(i["price"]))
#     count += 1
# # 2：用户输入选择的商品序号，然后打印商品名称及商品价格
#
# while 1:
#     number = input("请输入货号：")
#     if number == 'q'or number == 'Q' :   #4：用户输入Q或者q，退出程序。
#         break
#     else:
#         result = dic.get(number,"没有此货号,请重新输入：")
#         if result != "没有此货号,请重新输入：":#3：如果用户输入的商品序号有误，则提示输入有误，并重新输入。
#             print(result)
#             break
#         else:
#             print(result)

# 10.看代码写结果
#

v = {}
for index in range(10):
    v['users'] = index
print(v)
#
# 结果：v = {'users':9}
# ```
#
