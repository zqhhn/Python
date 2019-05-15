
class Student(object):
    # __init__ 是一个特殊方法用于在创建对象时进行初始化操作
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def study(self,course_name):
        print("%s正在学习%s"%(self.name,course_name))
    
    # PEP 8 要求标识符的名字用全小写多个单词用下划线连接
    def watch_tv(self):
        if self.age < 18:
            print("%s只能观看🐻"%self.name)
        else:
            print("%s可以随意观看"%self.name)

def main():
    stu = Student("fun",18)
    stu.study("English")
    stu.watch_tv()

if __name__ == "__main__":
    main()