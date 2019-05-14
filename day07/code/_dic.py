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