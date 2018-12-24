t1=(1,2,3,4,5,6,7)
t2=['ccb','icbc','boc','abc','poc','roc']
t3={'abc',123,90,'数据','88'}
t4={'ccb':105,"icbc":102,'boc':103,'abc':104,'信息':'info','姓名':'张三'}



'''
import pymysql
dbip = "192.168.66.103"
mydb = pymysql.conect("dbip","test","test","test")4[
cursor = db.cursor()
'''


abc=input("Please input you char:")
print("hello",abc)


a = input("please intpu a number:")
if int(a) >= 0:
    print(a)
else:
    print(-int(a))



a = 'ABC'
print(a)
b=a
a="123"
print(b)


c=divmod(15,7)
print(c)





bmi = int(input('Please input bmi:'))
if bmi<18.5:
    print('too light')
elif 18.5<=bmi<=20:
    print('nomal')
elif 25<bmi<=28:
    print('too heavy')
elif 28<bmi<=32:
    print('fat')
elif 32<bmi:
    print('too fat')
else:
    pass




for bank in ins:
    print("this is my bank",bank)

for i in range(101):
    num=num+i
print(num)('CCB')



def test_abs(x,y):
    print('the first agr is %s,\nthe second arg is %s.\n'%(x,y))
    if int(x)>int(y):
        return x,y
    elif int(x)<int(y):
        return y,x
    else:
        return 'err'


a=input('please input X:\n')
b=input('please input Y:\n')

c=test_abs(a,b)

print(c)




