from random import randint

def roll_dice(n=2):
    """
    掷色子
    :param n:色子的个数
    :return: n颗色子点数之和
    """
    total = 0
    for _ in range(n):
        total += randint(1,6)
    return total

def add(a=0,b=0,c=0):
    return a + b + c

# 如果没有指定参数 那么使用默认值
print(roll_dice())
print(roll_dice(3))
print(add())
print(add(1,2))
# 传递参数时可以不按照设定的顺序进行传递
print(add(c=1000,a=10,b=100))

def foo():
    print("hello,world!")

'''
def foo():
    print("goodbye, world!")
'''
foo()