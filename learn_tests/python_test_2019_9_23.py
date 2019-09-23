import os,sys
a = 5
b = 3
st = "a > b" if a > b else "a < b"
print(st)
print("a > b") if a > b else print("a < b")

c = 6
d = 6
print("c > d") if c > d else (print("c < d") if c < d else print("c == d"))

#st = print("crazyit"); x = 20 if a > b else ""
st = x = 20; print("crazyit") if a > b else ""
print(st)
print(x)
st = 20, print("crazyit") if a > b else ""
print(st[0])
print(st[1])

a_tuple = ("tuple...",)
b_tuple = ("str...")
print(type(a_tuple))
print(type(b_tuple))

a = {1, "c", 1, (1, 2, 3),"c"}
for ele in a:
    print(ele, end=" ")
print("")

str1 = "人生苦短，我用Python" #utf-8汉字和标点符号占三个字节，英文字符占1个字节
print(len(str1.encode()))
print(len(str1.encode("gbk"))) #gbk汉字和标点符号占2个字节, 英文占1个字节

data = [5,8,4,1]
for i in range(len(data) - 1):
    for j in range(len(data) - i - 1):
        if(data[j] > data[j+1]):
            data[j], data[j+1] = data[j+1], data[j]
print("排序后：", data)

###列表，元祖，字典，集合推导式
dictdemo = {"1":1, "2":2, "3":3}
newdemo1 = {x for x , y in dictdemo.items() if y >= 2}
print(newdemo1)
newdemo2 = {x for x in dictdemo.values() if x >= 2}
print(newdemo2)
newdemo3 = {x for x in dictdemo.keys()}
print(newdemo3)

reverse_demo = {v:k for k,v in dictdemo.items()}
print(reverse_demo)


## zip() 函数
books = ["java讲义", "python讲义", "c讲义"]
prices = [30,60]
for book, price in zip(books, prices):
    print("{0}的价格是:{1}".format(book, price))

## sorted()
a = [20, 30, -1.2, 3.5, 90]
sorted_list = sorted(a)
print(sorted_list)
sorted_list = sorted(a, reverse=True)
print(sorted_list)
b = ["f","cra","sd","dfsdfds","1d"]
sorted_list = sorted(b, key=len) #key=len,根据字符串长度进行从小到大排序
print(sorted_list)
sorted_list = sorted(b, key=len, reverse=True) #key=len,根据字符串长度进行从小到大排序,再倒排
print(sorted_list)

## reversed()
c = ["a",20,"fkit",1]
reversed_list = [x for x in reversed(c)]
print(reversed_list)

############################################################################################

import traceback
## try except else finally
def foo():
    fis = None
    try:
        fis = open("a.txt")
    except ValueError:
        print("数值错误")
    except ArithmeticError:
        print("算数错误")

    except OSError as e:
        print(e.strerror)
        return            #执行return语句后仍然会执行下面的finally块代码
        #os._exit(1)      #退出python解释器, 则不会执行下面的finally块代码
    except Exception as e:
        print("未知异常")
        print(e.args)     #访问异常的错误编号和详细信息
        print(e.errno)    #访问异常的错误编号
        print(e.strerror) #访问异常的详细信息
    except :#不带任何参数的except必须放到最后一个
        print(sys.exc_info())                   #返回type, value, traceback
        traceback.print_tb(sys.exc_info()[2])   #输出信息中包含了更多的异常信息，包括文件名、抛出异常的代码所在的行数、抛出异常的具体代码
        traceback.print_exc()                   #捕捉异常，并将异常传播信息输出控制台
        traceback.print_exc(file=open('log.txt', 'a')) #捕捉异常，并将异常传播信息输出指定文件中

    else:
        print("没有出现异常,程序正常执行...")

    finally:
        print("资源回收块")
        if fis is not None:
            try:
                fis.close()
            except OSError as ioe:
                print(ise.strerror)
        print("执行finally块里的资源回收!")
foo()

## raise 手动抛出一个异常
def f01():
    try:
        mtd(8)
    except Exception as e:
        print("程序出现异常：", e)
    #mtd(3)     #若不捕获程序抛出的异常，会导致程序终止
def mtd(a):
    if a < 5:
        raise
    if a > 6:
        raise ValueError("a的值大于0， 不符合要求")
f01()


### 自定义异常类
class SelfExceptionError(Exception):
    print("自定义异常类！")

try:
    raise SelfExceptionError()
except SelfExceptionError:
    print("自定义的异常")

class InputError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return ("{} is invalid input.".format(self.value))

try:
    raise InputError(1)
except InputError as err:
    print("error: {}".format(err))

import logging
#DEBUG, INFO, WARNING, ERROR, CRITICAL
logging.disable(logging.WARNING) #禁止该级别以及更低级别的所有日志消息
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s-%(levelname)s - %(message)s")
logging.debug("Start of program.")
logging.info("Start of program.")
logging.warning("Start of program.")
logging.error("Start of program.")
logging.critical("Start of program.")

#将日志信息追加写入到文件，既能使屏幕保持干净，又能保存信息
logging.basicConfig(filename="logging.txt", level=logging.DEBUG, format="%(asctime)s-%(levelname)s - %(message)s")

############################################################################################

### super()
class Employee:            #新式类，所有类都隐式继承object类
#class Employee(object):   #与上一行代码效果相同,object 作为所有基类的祖先
    def __init__(self, salary):
        self.salary = salary
    def work(self):
        print("普通员工正在写代码, 工资是:", self.salary)

class Customer(object):    #新式类，所有类都隐式继承object类
    def __init__(self, favorite, address):
        self.favorite = favorite
        self.address = address
    def info(self):
        print("我是一个顾客，我的爱好是%s, 地址是%s" %(self.favorite, self.address))

class Manager(Employee, Customer):
    def __init__(self, salary, favorite, address):
        super().__init__(salary)
        #super(Manager, self).__init__(salary) #与上一行代码效果相同
        Customer.__init__(self, favorite, address)
        print("--Manager 的构造方法--")

m = Manager(25000, "IT产品", "广州")
m.work()
m.info()

    
###super()
class Animal(object):
    def __init__(self, name):
        self.name = name
    def greet(self):
        print("Hello I am %s." % self.name)

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
    def greet(self):
        super().greet()
dog = Dog("dog")
dog.greet()


