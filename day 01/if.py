# # 1、猜年龄
# guess_age = input("请输入年龄：")
# shiji_age = '48'
# if guess_age > shiji_age:
#     print("输入年龄过大")
# elif guess_age < shiji_age:
#     print("输入年龄过小")
# else:
#     print("正确")
# # 2、再来个匹配成绩的小程序吧，成绩有ABCDE5个等级，与分数的对应关系如下
# # A    90-100
# # B    80-89
# # C    60-79
# # D    40-59
# # E    0-39
# #自己写的
# score = int(input("请输入分数："))
# if 90<= score <= 100:
#     print("A")
# elif 80 <= score <90:
#     print("B")
# elif 60 <= score <80:
#     print("C")
# elif 40 <= score < 60:
#     print("D")
# elif 0 <= score <40:
#     print("E")
# else:
#     print("输入错误")
#
# #节省算法 代码是从上到下依次判断，只要满足一个，就不会再往下走***
# score = int(input("请输入分数："))
# if score >100:
#     print("你太牛逼了")
# elif score >=90:
#     print("A")
# elif score >= 80:
#     print("B")
# elif score >= 60:
#     print("C")
# elif score >= 40:
#     print("D")
# elif score>=0:
#     print("E")
# else:
#     print("输入错误")
