# # fenshu = int(input('请输入学生分数'))
# #
# # if fenshu>100 or fenshu<0:
# #     print('输入有误！')
# # else:
# #     if fenshu>=90:
# #         print('A')
# #     if 80<=fenshu<90:
# #         print('B')
# #     if 60<=fenshu<80:
# #         print('C')
# #     if 0 <= fenshu <60:
# #         print('D')
#
# #三元操作符
#
# x,y = 4,5
#
# # if x<y:
# #     small = x
# # else:
# #     small = y
# # print(small)
# small = x if x<y else y
# print(small)
#
#
#
#
# assert 3>4

# qqq = 'gugong'
# for i in qqq:
#     print(i,end=' ')
#
# member = ['小甲鱼','晓不得','学习','努力']
# for each in member:
#     print(each,len(each),type(each))

# print(list(range(1,10,2)))
#
# bingo='顾工是及其厉害的程序员'
# answer = input('请输入顾工最喜欢的一句话')
#
# while True:
#     if answer == bingo:
#         break
#     answer =input('抱歉输入错误,请重新输入（答案正确才能退出游戏！）')
#
# print('不错哦！')
# print('你的评价很准确')

for i in range(10):
    if i%2 != 0:
        print(i)
        continue
    i +=2
    print(i)

for i in range(10):
    if i%2 != 0:
        print(i)
    else:
        i +=2
        print(i)


