#!usr/bin/python
"""age=3
name="tom"
print("我叫"+name+"今年已经"+str(age)+"岁了！")"""
"""import os
import requests
print(os.getcwd())
r=requests.get("https://api.shouqiev.com/h5/login.json?channelId=dlndc3")
print(r.url)
print(r.encoding)
print(r.text)"""
"""import sys
c=abs(-5-8)#取绝对值
print(c)
a=3
b=4
c=5.66
d=8.0
e=complex(c,d)
f=complex(float(a),float(b))
print("a is type",type(a),"c is type",type(c),"f is type",type(f))
print(a+b)
print(d//c)     #取整
print(f)
print(sys.float_info)#数据类型定义范围"""
# CTRL/    快速注释
# number_list=[1,2,1,3,5,8,6]
# print("number_list is"+str (number_list))
# str_list=["cbujd","ncdeu","cbjh",5,9]
# print("str_list is  "+str (str_list))
# del str_list[3]
# print("str_list is  "+str (str_list))
"""tuple是元组"""
# a_tuple=(2,)
# mixed_tuple=(1,2,['a','b'])
# print("mixed_tuple[2][0]:"+str(mixed_tuple[2][0]))
# phone_book={'Tom':123,'Jerry':456,'Kim':789}
# mixed_dict={'Tim':'boy',11:23.5}
# print(str(phone_book['Tom']))
# phone_book['Tom']=999;
# print(str(phone_book['Tom']))
# phone_book['Heath']=888
# print(str(phone_book))
# del phone_book['Tom']
# print(str(phone_book))
# del phone_book
# print(str(phone_book))

# rep_test={'name':12,'s':25,'name':38}
# print(rep_test)
"""函数的构造"""
# def repeat_str(s,times=1):
#     repeat_strs=s*times
#     return  repeat_strs
# rep=repeat_str("刘尚阳",4)
# print(rep)
"""函数要缩进"""
# def num_su(a,b=1,c=3):
#     print('a is',a,'b is',b,'c is',c)
# num_su(1,3,5)

# number=59
# guess=int(input('请输入一个数字：'))
# while(1):
#     if guess==number:
#         print('恭喜你输入对了')
#         break;
#     else:
#         print('请重新输入！')
#         guess = int(input('请输入一个数字：'))
# list_b=[1,3,5,7,9]
# for i in list_b:
#     print(i)
# else:
#     print('loop is over!')
"""打印字典"""
# lsy={'a':11,'b':55,'c':14}
# for i in lsy:
#     print(i)
#     print(lsy[i])
"""第17课已经看完"""
# a_list=[0,1,2]
# for i in a_list:
#     if not i:
#         continue    """回到循环体前"""
#     print(i)
# print('pass')
# for i in a_list:
#     if not i:
#         pass
#     print(i)

# str_1=input("请输入一个字符：")
# str_2=input("请再输入一个字符：")
# print("str_1+str_2",str_1+str_2)
"""写文件"""
# some_sentence="我喜欢你，但是我不会很努力！"
# # f=open('sentence.txt','w')
# # f.write(some_sentence)
# # f.close()

"""读文件"""
# f=open('sentence.txt')
# while True:
#     line=f.readline()
#     if len(line)==0:
#         break
#     print(line)
# f.close()

"""19课"""
"""处理异常"""
# while True:
#     try:
#         x=int(input("请输入一个数字："))
#         break
#     except ValueError:
#         print("请重新输入：")
"""如果没有出现异常，就不会执行except后面的语句"""
# try:
#     f=open('shi.txt')
# except OSError as err:
#     print("OSError:{0}".format(err))

"""20课   面向对象编程
类------class
类对象
实例对象

装饰器

类
"""

# class student:
#     def __init__(self,name,grade):            #具体实例化
#         self.name=name
#         self.grade=grade
#     def introduce(self):
#         print('我叫'+self.name)
#         print('我的成绩是'+str(self.grade))
#     def improve(self,amout):
#         self.grade=self.grade+amout
# jim=student('jim',86)
# jim.introduce()
#
# jim.improve(10)
# jim.introduce()
# def add_candles(cake_func):
#     def insert_candles():
#         return cake_func + "candles"
#     return insert_candles()
# def make_cake():
#     return "cake"
# gift_func=add_candles(make_cake())
# print(make_cake())
# print(gift_func)

# def add_candles(cake_func):
#     def insert_candles():
#         return cake_func() + " and candles"
#     return insert_candles
# @add_candles        #装饰器
# def make_cake():
#     return "cake"
#
# print(make_cake())


"""
8.1         图形界面（GUI）和猜数字游戏
GUI : graphical user interface
# """
# from tkinter import *
# import tkinter.simpledialog as dl           #简单对话框
# import tkinter.messagebox as mb         #信息框
# root=Tk()
# w=Label(root,text='小例程')
# w.pack()        #自适应
# number=50
# mb.showinfo("welcome","welcome to guess game!")
# while True:
#     guess=dl.askinteger("number","请输入一个数字：")
#     if guess==number:
#         mb.showinfo('结果','恭喜你猜对了！')
#         break
#     elif guess<number:
#         mb.showinfo('结果','你猜的数据有点小呦！')
#     else:
#         mb.showinfo('结果','你猜的数据有点大呦！')
# mb.showinfo('OVER', '游戏结束了' )
#
# class Test:
#     pass            #空的类
# Test()
# class Text:
#     def pr(self):
#         self.height=20
#         print(self.height)
#
# tca=Text()
# tca.pr()
#
# class tcc:
#     """
#     这是一个空类!
#     """
#     pass
# help(tcc)

"""面向对象  第4课已经看完"""

# mylist=["one","two"]
# # print(mylist)
# # mylist.append("Three")
# # print(mylist)
#  is判断
# name="top"
# test="to"
# print(name is test)

# a=input("请输入一个数：")
# print(a)
# #第6集已经看完
# def pName(name):
#     print("我叫MousuSun!\r\n")
#     print(name)
# pName("刘尚阳\r\n")
##第10课已经看完了
# l3=[('a',123),('b',56),('c',"刘尚阳")]
# print(l3)
# d1=dict(l3)
# print(d1)
'''
ord(x)  ---将字符转换为整数值
oct(x)   ---转换成8进制
bin(x)  ---转换成二进制
'''

# x=9
# std=bin(x)
# print(std)

# num1=2
# print(num1)
# num1<<=2
# print(num1)

# num1=(1+0.01)**365
# print(num1)
# import math
# num2=math.sqrt(163)
# print(num2)

# def priname():
#     '''tets15ed15vvre
#     cfnhewuhvioe
#     vrewihi'''
#     print("hello")
# print(priname.__doc__)
# s=[1,2,5,6,4,8,2,3,5,45]
# print(len(s))


'''2018/8/12
第14课已经看完
'''
'''连接字符串'''
# tr=['h','e','l','l','o']
# tr='-'.join(tr)
# print(tr)

'''字符串分割'''
# tr="zuijiaoshangyanh"
# ty=tr.split('jiao')
#  print(ty)
'''字符串修剪'''
# tr="     hello"
# tr=tr.strip('o')
# print(tr)

# l1=[12,25,1,2,3]
# l1[1:3]=[]
# print(l1[1])
# l1=[12,25,1,2,3]
# del(l1[1:])
# print(l1)
# l2=[1,2,3,4,5,2,8,9]
# l2.append(100)
# l4=l2.count(2)#计算某一个元素出现的次数
# print(l4)

# l1=['x','y','z']
# l2=[1,2,3,4]
# l2.extend(l1)#作为单个元素加入列表
# print(l2)

# l1=[1,2,3]
# l1.insert(1,22)#插入
# l1.pop(2)#弹出某一个索引对应的值  2为索引
# print(l1)

# l1=[2,2,3,4,2,5,5,222]
# l1.remove(2)
# print(l1)

# l1=[22,33,55,[2,3,5,],'cbsy']
# print(l1)
# l1.reverse()
# print(l1)
# l1=[1,2,3,55]
# l2=[255,26,5]
# l3=l1+l2
# print(l3)

# tr1="hello"
# tr="llll"
# str=tr1+tr
# print(str*2)
'''成员关系判断  in  -----not in'''
# l1=[2,5,3,8,6,16]
# ll=20 not in l1
# print(ll)

# l1=[1,2,3]
# l2=l1[:]
# print(l1)
# l1.append(25)
# print(l1)
# print(l2)

'''复制列表'''
# import copy
# l1=123
# l2=copy.deepcopy(l1)
# l1=456
# print(l2)

'''元组tuple'''
# t1=(1,2,3,4,5,6,852)
# t2=t1.index(852)
# print(t1*2)

# t3=('x',[1,2,3,4,2,6,6])
# print(t3)
# t3[1].pop()
# print(t3[1])
'''字典 dict 键 值 key value
字典在其他编程语言中有称作关联数组或散列表
通过键来实现元素的存取---无序集合---可变类型容器--异构--嵌套

{ key1:value1，key2:value2,...}
{}--空字典
'''

# d1={'x':32,'y':[2,3,4,45]}
# print(d1['y'][3])
# print(len(d1))
# d1['x']=1200
# print(d1)
# d1={'m':123,'s':22,'d':45}
# l1=d1.get('s')
# print(l1)
# l1=d1.items()
# print(l1)
# l1=d1.values()
# print(l1)
# d1.popitem()
# print(d1)
'''合并两个字典'''
# d2={'e':20,'jk':56}
# d1.update(d2)
# print(d1)
# print(d2)

'''19集已经看完....2018/8/13'''
'''快速构建字典'''
# l1=zip('xya','123')
# print(dict(l1))
#
# x=3
# y=callable(x)
# def prix():
#     print("hello")
# z=callable(prix())
# print(z)

'''
列表---[]
元组---()
字典---{}
'''

# l1=[2,5,4,6,1,3,9]
# l1.sort()
# print(l1)
# l1.reverse()
# print(l1)

# d1={'x':1,'y':2}
# l1=d1.__iter__()
# l2=l1.__next__()
# print(l2)
# l1=[1,2,3,4]
# l2=dir(l1)
# print(l2)


# l1=set([1,5,2,6,4])
# l2=set([2,5,7,88,25])
# l3=l1.difference(l2)
# print(l3)
# l4=l1.intersection(l2)
# print(l4)
# l5=l1 | l2
# print(l5)
# l6=l1 & l2
# print(l6)



# s1=set([1])
# s1.add('lsy')
# print(s1)
'''获取对象的引用计数'''
# import sys
# name='lsy'
# l2=sys.getrefcount(name)
# print(l2)


'''列表和字典都支持两种类型的复制操作---浅复制和深复制
深复制--申请形容存储空间---使用copy模块中的deepcopy()
浅复制--指向同一个内存空间
'''
'''/---除法
    //--取整
'''
# a=4//3
# print(a)

'''逻辑运算---or  and not 
    位运算--- | & ^ << >>

三元选择表达式
x if y else z   y为条件

匿名函数的表达式：lambda args:expression

生成器函数发送协议： yield x



'''

# print('xx') if 2>1 else print('hello!')


'''第24集已经看完   2018/8/14'''

'''
if/elif/else:----条件判断
for/else:---序列迭代
while/else:普通循环
pass:占位符
break;
continue
def
return
yield
global:命名空间
raise:触发异常
import:
from:模块属性访问
class:类
try/except/finally:捕捉异常
del:删除引用
assert:调试检查
with/as:环境管理器
'''
'''分解赋值'''
# l1=('Sun','Sat','Mon')
# x,y,z=l1
# print(x)
# print(y)

'''python 流程控制语句----if
if 条件测试表达式
测试操作符----
== 操作符测试值的相等性
is 表达式测试对象的一致性

'''
# x=1
# y=2
# if x>y:
#     print('the max num is %d'%x)
# else:
#     print("the min num is %d"%y)

# url='wwwbaiducom'
# while url:
#     print(url)
#     url=url[1:]

# x=0;y=100
# while x<y:
#     print(x)
#     x+=2

# url='wwwbaiducom';x=0
# while url:
#     print(url)
#     url=url[:-1]
# else:print('game over')
'''
while bool_expression
    while_suite
    else:
        else_suite
    break:跳出最内层的循环
    continue：调到所处的最近层循环的开始处
    pass：点位语句
    else:循环正常终止才会执行，如果循环终止是由BREAK跳出导致的，则ELSE不会执行

'''
# while url:
#     print(url)
#     url=url[:-1]
#     x+=1
#     if(x>7):
#         break
# else:print('game over')
'''第27集已经看完----2018/8/15'''
'''第28集已经看完----2018/10/26'''
# test=[]
# while True:
#     x=input("Enter num\n")
#     if x=='q':
#         break
#     test.append(x)
#     print(test)
# d1={'x':123,'y':22,'z':586}
# for(k,v) in d1.items():
#     print(k,v)
# l1=["sun","dea","gyg","hdue"]
# # for i in range(0,len(l1)):
# #     print (l1[i])
# l2=iter(l1):
# l2=[]
# for i in l1:
#     l2.append(i**2)
# print(l2)
# 列表解析是python迭代机制的一种应用，实现创建新的列表
# temp=0
# for i in [i**2 for i in range(1,2)]:
#     temp+=i
# print(temp/2)
#
# f1=open('I:\\Users\\doc_test\\158.PLT','r+',-1)
# print(f1.readline())
# print(f1.tell())    #统计文本的字节数
# # f1.seek(11000)  #移动文件指针
# # print(f1.readline())
# print(f1.read(10))
# print(f1.tell())
# str=f1.name
# print(str)
# f1.seek(0,2)
# print(f1.tell())
# f1.write('你好---\n')
# f1.close()
# f1=open('I:\\Users\\doc_test\\158.PLT','r',-1)
# print(f1.readline())
# f1.close()
# f2=open('I:\\Users\\doc_test\\text.txt','w+',-1)
# for line in(i**2 for i in range(1,11)):
#     f2.write(str(line)+'\n')
# f2.close()
# l1=[i**2 for i in range(1,11)]
# print(l1)
