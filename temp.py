# _*_ coding: utf-8 _*_
def test_abs(name, age, gender='Man', city='Beijing'):
    print(name, age, gender, city)


test_abs('jack', '24', 'M', 'beiing')


def test1(*number):
    print(number)


def test2(name, age, **kwargs):
    print('name:', name, 'age', age, 'others', kwargs)
    if 'city' in kwargs:
        print('city:', kwargs['city'])


test2('jack', '25', gerder='M', city='beijing', country='CN')


def test3(name,age,CCB,BOC,ICBC):
    print(name,age,CCB,BOC,ICBC)

test3('tom','24',*e)





def test4(*args):
    if len(args)==0:
        return "null number"
    y=1
    for x in args:
        y=y*x
    return y


def test5(n):
    if n==1:
        return 1
    return n*test5(n-1)

a='abcdef'



def test6(args):
    i=0
    j=-1
    while args[i]==' ':
        i=i+1
        continue
    while args[j]==' ':
        j=j-1
        continue
    print('i is %d,\nj is %d'%(i,j))
    return args[i:j+1]

for key in e:
    print(key.value)


for i,key in enumerate(a):
    print(i,key)

def test7(*args):
    print(len(args))
    print(args)
    min=0
    max=0
    for i in range[args]:
        if max<i:
            max=i
        elif min>i:
            min=i
        else:
            pass
    print('max:',max,'\nmin:',min)
    return(max,min)

t=test7(*a)



def test8(args):
    print(len(args))
    print(args)
    min=args[0]
    max=args[0]
    for i in args:
        if i>max:
            max=i
        elif i<min:
            min=i
        else:
            print('middle number')
    print('max is:',max)
    print('min is:',min)
    rul=(max,min)
    return(rul)

'''function'''
def fib(max):
    n,a,b,=0,0,1
    l=[]
    while n<max:
        print(b)
        a,b=b,a+b
        n=n+1
        l.append(b)
    return l

'''generator'''
def fib(max):
    n,a,b,=0,0,1
    l=[]
    while n<max:
        yield b
        a,b=b,a+b
        n=n+1
        l.append(b)
    return l


def odd():
    print('setp 1')
    yield 1
    print('step 2')
    yield 3
    print('step 3')
    yield 5

def newlist(L):
    newlist=[]
    newlist.append(1)
    n=len(L)
    if len(L)==0:
        return(newlist)
    i=1
    while i<=n-1:
        newlist.append(L[i-1]+L[i])
        i=i+1
    newlist.append(1)
    return(newlist)

def tri():
    L=[]
    while True:
        L=newlist(L)
        yield L
    print('end')


def f(x):




















