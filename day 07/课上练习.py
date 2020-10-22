# # #删除索引为奇数位的元素
# # l1 = [115,11,22,33,44,55]
# # for i in range(len(l1)):#这种方法会报错，pop index out of range  原因每循环一次删除一个元素，列表索引长度就会变小
# #     if i % 2 == 1:
# #         print(i)
# #         l1.pop(i)
# # print(l1)
# # del l1[1::2]
# # print(l1)
#
# # 将字典中键含有'k'元素的键值对删除。
# dic = {'k1': '太白', 'k2': 'barry', 'k3': '白白', 'age': 18}
# # for i in dic:
# #     if 'k' in i:
# #         dic.pop(i)
# # print(dic)
#
# for i in list(dic.keys()):
#     if 'k' in i:
#         dic.pop(i)
# print(dic)