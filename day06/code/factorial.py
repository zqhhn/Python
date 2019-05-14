'''
求阶乘
:param num: 非负整数
:return: num的阶乘
'''
def factorial(num):
    result = 1
    for n in range(1,num + 1):
        result *= n
    return result

if __name__ == "__main__":
    print("5的阶乘:",factorial(5))