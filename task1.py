# # 1、变量与参数的传递
# a=[1,2,3]
# b=a
# c=list(a)
# print(a)
# print(b)
# print(c)
# print("***********")
# b[1]= 100
# c[2]= 500
# print(a)
# print(b)
# print(c)
# if a is b:
#     print("a and b are the same memory")
# else: print("diff")
# if a is c:
#     print("they're same")
# else: print("diff")
#
# #2、运用函数识别变量类型。——变量的引用不涉及类型，变量的类型是动态的，变量本身是由类型的
# a_2 = [1,2,3]
# print(type(a_2))
# if isinstance(a_2,list):
#     print("yes!")
# else: print("no!")
#
# #3、格式符%
# import math
# print("20+10的结果为%d"%(20+10))
# name = input("what is ur name? \n")
# height = int(input('how tall are u \n'))
# #注意：input的输出都是字符串类型
# print("hi! dear %s, I know you are %d cm"%(name,height))
# print("this num is %5f"%math.pi)
#
# #4、二元运算符和比较符
# a_4 = 8
# b_4 = 2
# print(a_4+b_4)
# print(a_4**b_4)
# print(a_4//b_4)
# print(a!=b)
# c_4 = None
# print(c_4 is not None)
#
# #5、数值类型 与 强制转换
# a_5 = 100
# b_5 = '3+55d'
# print("type of num_5 is",type(a_5))
# print("type of num_5 is",type(b_5))
# #相比于上面的%模板类型，%可以插入多个模板数据
# print(int(math.e))
# print(float(20))
# #6、字符串储存以后不能直接更改字符串中的某一个元素，字符串是不可变对象，但可以拼接,拼接以后会产生一个新的内存
# c_5 = "barren"
# print(c_5[3:6])
# d_5 = c_5[:5]+'l'
# print(d_5)
# print(c_5+'aaa')
# print(c_5*2)
# print('ren' in c_5)
# print(c_5.find('r'))
# print(c_5.replace("n","l"))
# print(c_5.count('r'))
# print(c_5.upper())
# shuliang = 6
# fruit = 'banana'
# jiage= 0.66
# print('%d %s cost %.2f dollars'%(shuliang,fruit,6*jiage))
# names= input('what is ur name? \n')
# if len(names)>8:
#     print('ur name is so long!')
# else:print('just a short name!')
#
# #7、if、for、while 的具体运用
# num1 = int(input('please input a num \n'))
# if 0:
#     print('this is true')
# else:print('is false')
# total = 0
# for i in range(5):
#     square=i*i
#     total =total + square
# print(total)
# sum = 0
# for num2 in range(2,101,2):
#     sum = sum+num2
# print(sum)
#
# classcounter =1
# classtotal = 0
# while classcounter <=2:
#     gradetotal =0
#     stucounter = 0
#     grade = input('enter grade -1 to2: \n')
#     grade = int(grade)
#     while grade !=-1:
#         #这里，因为grade是一次一次输入的，如果输入了-1就表示该循环结束，可以进行下一个循环了。表示该种方法可以终止输入类型的循环
#         gradetotal += grade
#         stucounter += 1
#         grade = input('enter grade -1 to2: \n')
#         grade = int(grade)
#         #第一个while循环中输入第一个grade是为了打开进入第二个while循环，
#     if classcounter != 0:
#         average = float(gradetotal/stucounter)
#         print('class %d average grade id %.3f'%(classcounter,average))
#     else:
#         print("no grades were entered ")
#     classcounter +=1
#
# #8、continue和break的用法
# for a_8 in range(5):
#     if a_8==3:
#         continue
#     if a_8==4:
#         break
#     print(a_8)
#
# #9、元组固定了长度，一旦创建就不能再修改。因此特殊情况下（例如函数的因变量）会用元组。
# # #list用[]，元组用（）,元组可用拆包“更改”元素,元组交换元素可以直接赋值
# a_9 =(0,'a',False)
# b_9 = (False,None)
# print(a_9+b_9)
# print(b_9*3)
# d,e,f =a_9
# print(e)
# c_9,d_9 = 8,6
# d_9,c_9=c_9,d_9
# print(d_9)
# #用于抽取列表中某一列的元素
# seq = [(1,2,3),(4,5,6),(7,8,9)]
# for e_9,f_9,g_9 in seq:
#     #字符串相关——调用字符串函数.format(),且大括号{}表示模板调用字
#     print('e_9={0},f_9={1},g_9={2}'.format(e_9,f_9,g_9))
# be_list = list(a_9)
# print(be_list[0])
# print(b_9[0])
# print(a_9)
# #10、列表，列表在原本内存上更改的,zip函数
# a_10 = [0,2,4,9]
# b_10 = [False,10]
# c_10 = [4,18,5,7,3,9,2]
# a_10.extend(b_10)
# print(a_10)
# c_10.sort()
# print(c_10)
# d_10 =['idlo','am','handsome','pretty']
# d_10.sort(key=len)
# print(d_10)
# i=0
# for value in d_10:
#     print('list中第{0}个值是{1}'.format(i,value))
#     i+=1
# print('************************')
# for i,value in enumerate(d_10):
#     print('list中第{0}个值是{1}'.format(i, value))
#
# e_10=zip(a_10,d_10)
# print(type(e_10))
# print(e_10)
# print(list(e_10))
# aa_10,dd_10=zip(*e_10)
# print(dd_10)
# f_10=zip(a_10,b_10)
# print(list(f_10))
# zip函数的鲁棒性
#
# 朴素贝叶斯的代码
# import pandas as pd
#
# def createDataSet_2():
#     dataSet_2 = [
#         # 1
#         ['青绿', '蜷缩', '浊响', '清晰', '凹陷', '硬滑', '好瓜'],
#         # 2
#         ['乌黑', '蜷缩', '沉闷', '清晰', '凹陷', '硬滑', '好瓜'],
#         # 3
#         ['乌黑', '蜷缩', '浊响', '清晰', '凹陷', '硬滑', '好瓜'],
#         # 4
#         ['青绿', '蜷缩', '沉闷', '清晰', '凹陷', '硬滑', '好瓜'],
#         # 5
#         ['浅白', '蜷缩', '浊响', '清晰', '凹陷', '硬滑', '好瓜'],
#         # 6
#         ['青绿', '稍蜷', '浊响', '清晰', '稍凹', '软粘', '好瓜'],
#         # 7
#         ['乌黑', '稍蜷', '浊响', '稍糊', '稍凹', '软粘', '好瓜'],
#         # 8
#         ['乌黑', '稍蜷', '浊响', '清晰', '稍凹', '硬滑', '好瓜'],
#         # 9
#         ['乌黑', '稍蜷', '沉闷', '稍糊', '稍凹', '硬滑', '坏瓜'],
#         # 10
#         ['青绿', '硬挺', '清脆', '清晰', '平坦', '软粘', '坏瓜'],
#         # 11
#         ['浅白', '硬挺', '清脆', '模糊', '平坦', '硬滑', '坏瓜'],
#         # 12
#         ['浅白', '蜷缩', '浊响', '模糊', '平坦', '软粘', '坏瓜'],
#         # 13
#         ['青绿', '稍蜷', '浊响', '稍糊', '凹陷', '硬滑', '坏瓜'],
#         # 14
#         ['浅白', '稍蜷', '沉闷', '稍糊', '凹陷', '硬滑', '坏瓜'],
#         # 15
#         ['乌黑', '稍蜷', '浊响', '清晰', '稍凹', '软粘', '坏瓜'],
#         # 16
#         ['浅白', '蜷缩', '浊响', '模糊', '平坦', '硬滑', '坏瓜'],
#         # 17
#         ['青绿', '蜷缩', '沉闷', '稍糊', '稍凹', '硬滑', '坏瓜']
#     ]
#
#     # 特征值列表
#     labels_2 = ['色泽', '根蒂', '敲击', '纹理', '脐部', '触感', '好瓜']
#     return dataSet_2, labels_2
#
# def Naivebayes(test):
#     data= ['青绿', '蜷缩', '沉闷', '稍糊', '稍凹', '硬滑']
#     data = data.values.tolist()
#     goodMelon =[];badMelon=[]
#     for i in range(len(data)):
#         if data[i][8]==1:
#             goodMelon.append(data[i])
#         else:
#             badMelon.append(data[i])
#     p1 = 1.0;p2 = 1.0
#     for j in range(len(test)):
#         x=0.0
#         for k in range(len(goodMelon)):
#             if goodMelon[k][j]==test[j]:
#                 x+=1.0
#         p1=p1*((x+1.0)/(len(goodMelon)+2.0))
#         #拉普拉斯平滑
#     pc1 = len(goodMelon)/len(data)
#     pc2 = 1-pc1
#     #贝叶斯公式
#     p_good = p1*pc1;p_bad = p2*pc2
#     if p_good>p_bad:
#         print('好瓜')
#     else:
#         print('坏瓜')
#
