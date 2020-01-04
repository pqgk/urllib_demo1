import copy
# member = ['小甲鱼','小布丁','黑夜','咪兔','意境']
# print(member)
#
# mix = ['1','小甲鱼',3.14,[1,2,3]]
# print(mix)
#
# empty = []
# #添加元素的方法
# empty.append('你好周杰伦')
# empty.append('朱晶晶')
#
# empty.extend(['qqq','ddd'])
# print(empty,len(empty))
#
# empty.insert(0,'asd')
# print(empty,len(empty))

member = ['小甲鱼','黑夜','迷途','怡景','秋舞斜阳']
member.insert(1,88)
member.insert(3,90)
member.insert(5,85)
member.insert(7,90)
member.insert(9,88)
# nian = [88,90,85,90,88]
# for each in nian:
#     member.append(each)

# for each in member:
#     print(each)



# print(member[0],member[1])
# print(member[2],member[3])
# print(member[4],member[5])
# print(member[6],member[7])
# print(member[8],member[9])

# i=0
# while i < 10:
#     print(member[i],member[i+1])
#     i = i+2


# for i in range(0,9,2):
#     print(member[i], member[i + 1])
#
# print(member[0])
# print(member[2])
#
# temp = member[0]
# member[0] = member[2]
# member[2] =temp
# print(member)
#
# #删除方法
# member.remove('迷途')
# print(member)
#
# del member[1]
# print(member)
#
# print(member.pop(0))
# print(member)
#
# copy=member[1:5]
# print(copy)

# print(member)
# sc = []
# while len(member)>0:
#     end = member.pop()
#     sc.append(end)
# print(sc)
#
# print(sc[-5:-2])
#
# print(dir(list))
#
# list = [123,456,789]
#
# list *=5
# print(list)
# print(list.count(123))
#
# print(list.index(456,3,20))

# print(member)
# list = [1,5,4,3,7,9,6]
# list.sort(reverse=True)
# print(list)

# old = [1,2,3,4,5]
# new = old
# old = [6]
# print(new)
# print(old)
#
# list1 = [1, [1, 2, ['小甲鱼']], 3, 5, 8, 13, 18]
# list2=list1.copy()
#
# list1[1][2][0] = '小鱿鱼'
# list1.remove(3)
# list1[1][2].append('nihao')
# list1.extend(['ni','zou','le' ])
# print(list2)
# print(list1)
# list1.clear()
# print(list1)


c = [ i*i for i in range(10) ]
print(c)

# list1 = [(x, y) for x in range(10) for y in range(10) if x%2==0 if y%2!=0]
# print(list1)
# list1 = []
# for x in range(10):
#     for y in range(10):
#         if (x%2==0) and (y%2!=0):
#             list1.append((x,y))
# print(list1)

list1 = ['1.Just do It','2.一切皆有可能','3.让编程改变世界','4.Nothing is impossible']
list2 = ['4.阿迪达斯','2.李宁','3.鱼c','1.耐克']

list3 = [list2[int(-i)]+list1[i][2:] for i in range(4)]
print(list3)
list4 = [name + '：' + slogan[2:] for slogan in list1 for name in list2 if slogan[0] == name[0]]
print(list4)
for each in list3:
    print(each)

list2.sort()
for i in range(4):
    print(list2[i],list1[i][2:])
    i +=1

for each in list2:
    for each2 in list1:
        if each[0] == each2[0]:
           print(each + ':' +each2[2:])

