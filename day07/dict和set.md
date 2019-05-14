#### 使用dict和set
##### dict
Python内置了字典：dict(dictionary)的支持,使用键-值(key-value)存储，具有极快的查找速度。
```Python
"""
把数据放入dict的方法，除了初始化时指定外，还可以通过key放入
    
1.通过in判断key是否存在
2.dict提供的get()方法，如果key不存在，可以返回None，或者自己指定的value：


"""
user_dic = {"wang":18,"MR":19}
# print(user_dic["wang"])
user_dic["wang"] = 28
# print(user_dic["wang"])
# 把数据放入dict的方法，除了初始化时指定外，还可以通过key放入
user_dic["zhong"] = 13
# print(user_dic["zhong"])
# 通过in判断key是否存在
# dict提供的get()方法，如果key不存在，可以返回None，或者自己指定的value：
if "zhong" in user_dic:
    print(user_dic["zhong"])
print(user_dic.get('xxx'))
print(user_dic.get('xxx','xxx'))

# 要删除一个key，用pop(key)方法，对应的value也会从dict中删除：
user_dic.pop("zhong")
print(user_dic.get('zhong'))
```
###### 和list比较，dict有以下几个特点:
1. 查找和插入的速度极快，不会随着key的增加而变慢。
2. 需要占用大量的内存，内存浪费多。
而list 相反：
1. 查找和插入的时间随着元素的增加而增加
2. 占用空间小，浪费内存很少。

dict是用空间换取时间的一种方法。

##### set
set和dict类似，也是一组key的集合，但不存储value.由于key不能重复,在set中没有重复的key
要创建一个set,需要提供一个list作为输入集合
```shell
s = set([1,2,3])
s
```
```Python

```