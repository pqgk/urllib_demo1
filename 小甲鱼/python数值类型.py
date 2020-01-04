# #python数据类型
# '520' + '1314'
#
# #整型、布尔型、浮点型、e记法
# a=0.000000000000000000000000025
# print(a)
#
# b=150000000000000
# print(b)
#
# c = 1.5e11
# print(c)
#
#
#
# #int()、str()、
#
# x = 5.99
# y = int(x)
# print(y)
#
# aa = 520
# bb =float(aa)
# print(bb)
#
# #type函数
#
# qq= '520'
# print(type(qq))
#
# #isintance
#
# qa = 'gugong'
# print(isinstance(qa,str))

a=input('请输入字符')
if isinstance(a,int):
    print('您输入的是数字')
else:
    print('您输入的不是数字')