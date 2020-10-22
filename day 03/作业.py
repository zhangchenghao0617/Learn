# # 1.有变量name = "aleX leNb" 完成如下操作：
# name = "aleX leNb"
# # - 移除 name 变量对应的值两边的空格,并输出处理结果
# print(name.strip())
# # - 判断 name 变量是否以 "al" 开头,并输出结果
# print(name.startswith('al'))
# # - 判断name变量是否以"Nb"结尾,并输出结果
# print(name.endswith('Nb'))
# # - 将 name 变量对应的值中的 所有的"l" 替换为 "p",并输出结果
# print(name.replace('l','p'))
# # - 将name变量对应的值中的第一个"l"替换成"p",并输出结果
# print(name.replace('l','p',1))
# # - 将 name 变量对应的值根据 所有的"l" 分割,并输出结果。
# print(name.split('l'))
# # - 将name变量对应的值根据第一个"l"分割,并输出结果。
# print(name.split('l',1))
# # - 将 name 变量对应的值变大写,并输出结果
# print(name.upper())
# # - 将 name 变量对应的值变小写,并输出结果
# print(name.lower())
# # - 判断name变量对应的值字母"l"出现几次，并输出结果
# print(name.count('l'))
# # - 如果判断name变量对应的值前四位"l"出现几次,并输出结果
# print(name.count('l',0,4))
# # - 请输出 name 变量对应的值的第 2 个字符?
# print(name[1])
# # - 请输出 name 变量对应的值的前 3 个字符?
# print(name[0:3])
# # - 请输出 name 变量对应的值的后 2 个字符?
# print(name[-2:])
#
# # 2.有字符串s = "123a4b5c"
# s = "123a4b5c"
# # - 通过对s切片形成新的字符串s1,s1 = "123"
# print(s[0:3])
# # - 通过对s切片形成新的字符串s2,s2 = "a4b"
# print(s[3:6])
# # - 通过对s切片形成新的字符串s3,s3 = "1345"
# print(s[0:7:2])
# # - 通过对s切片形成字符串s4,s4 = "2ab"
# print(s[1:6:2])
# # - 通过对s切片形成字符串s5,s5 = "c"
# print(s[-1:])
# # - 通过对s切片形成字符串s6,s6 = "ba2"
# print(s[-3:-8:-2])
#
# # 3.使用while和for循环分别打印字符串s="asdfer"中每个元素。
# s="asdfer"
#   while:
# i = 0
# while i < len(s):
#     print(s[i])
#     i+=1
#   for
# for i in s:
#     print(i)
#
# # 4.使用for循环对s="asdfer"进行循环，但是每次打印的内容都是"asdfer"。
# s="asdfer"
# for i in s:
#     print(s)
#
# # 5.使用for循环对s="abcdefg"进行循环，每次打印的内容是每个字符加上sb， 例如：asb, bsb，csb,...gsb。
# s="abcdefg"
# for i in s:
#     print(i.join('sb'))
#
# for i in s:
#     print(i + 'sb')
#
# # 6.使用for循环对s="321"进行循环，打印的内容依次是："倒计时3秒"，"倒计时2秒"，"倒计时1秒"，"出发！"。
# s="321"
# for i in s:
#     print('倒计时'+ i +'秒！')
# print('出发！')
#
# # 7.实现一个整数加法计算器(两个数相加)：如：content = input("请输入内容:") 用户输入：5+9或5+ 9或5 + 9，然后进行分割再进行计算。
# content = input("请输入内容:")
# content_space = content.replace(' ','')
# print(content_space)
# list = content_space.split('+')
# print(list)
# sum = 0
# for i in list:
#     sum = sum + int(i)
# print(sum)
#
# # 8.实现一个整数加法计算器（多个数相加）：如：content = input("请输入内容:") 用户输入：5+9+6 +12+ 13，然后进行分割再进行计算。
# content = input("请输入内容:")
# content_space = content.replace(' ','')
# print(content_space)
# list = content_space.split('+')
# sum = 0
# for i in list:
#     sum = sum + int(i)
# print(sum)
# # 9.计算用户输入的内容中有几个整数（以个位数为单位）。如：content = input("请输入内容：") # 如fhdal234slfh98769fjdla
# str = '1234a'
# content = 0
# for i in str:
#     if i.isdecimal() :
#         content +=1
# print(content)
#
#
#
# # 10.选做题**：写代码，完成下列需求：用户可持续输入（用while循环），用户使用的情况：
# # 输入A，则显示走大路回家，然后在让用户进一步选择：
# # 是选择公交车，还是步行？
# # 选择公交车，显示10分钟到家，并退出整个程序。
# # 选择步行，显示20分钟到家，并退出整个程序。
# # 输入B，则显示走小路回家，并退出整个程序。
# # 输入C，则显示绕道回家，然后在让用户进一步选择：
# # 是选择游戏厅玩会，还是网吧？
# # 选择游戏厅，则显示 ‘一个半小时到家，爸爸在家，拿棍等你。’并让其重新输入A，B,C选项。
# # 选择网吧，则显示‘两个小时到家，妈妈已做好了战斗准备。’并让其重新输入A，B,C选项。
# while 1 :
#     print('A:走大路，B：走小路,C:绕道')
#     choice = input('请输入：')
#     choice_upper = choice.upper()
#     if choice_upper == 'A':
#         print('你选择了走大路')
#         choice1 = input('请选择A:坐公交，B：走路:')
#         choice_upper1 = choice1.upper()
#         if choice_upper1 == 'A':
#             print('坐公交，十分钟后到家')
#             break
#         else:
#             print('走路回家，二十分钟后到家')
#             break
#     elif choice_upper == 'B':
#         print('你选择了走小路')
#         break
#     else:
#         print('你选择了绕道')
#         choice2 = input('请选择A:区游戏厅，B：去网吧:')
#         choice_upper2 = choice2.upper()
#         if choice_upper2 == 'A':
#             print('一个半小时到家，爸爸在家，拿棍等你。')
#         else:
#             print('两个小时到家，妈妈已做好了战斗准备。')
#
# # 1.写代码：计算1 - 2 + 3 - 4 + 5 - 6... + 99中除了88以外所有数的总和？
# s1 = 0
# s2 = 0
# i = 1
# while i <= 99 :
#     if i % 2 == 0:
#         if i == 88:
#             i += 1
#             continue
#         else:
#             s1 -= i
#     else:
#         s2 += i
#     i += 1
# print(s1+s2)
#
# # 2. ** 选做题： ** 选做题：判断一句话是否是回文.回文: 正着念和反着念是一样的.例如, 上海自来水来自海上
# str = input('请输入:')
# if str[-1::-1] == str:
#     print("是")
# else:
#     print('不是')
#
# # 3.制作趣味模板程序需求：等待用户输入名字、地点、爱好，根据用户的名字和爱好进行任意现实,如：敬爱可亲的xxx，最喜欢在xxx地方干xxx
# your_name = input('请输入姓名')
# your_place = input('请输入地点')
# your_hobby = input('请输入爱好')
# msg = '可亲的{name}，最喜欢在{place}地方干{hobby}'.format(name = your_name,place = your_place,hobby = your_hobby)
# print(msg)