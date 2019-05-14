#### 使用lis和tuple
##### list
python内置的一种数据类型是列表：list。list是一种有序的集合，可以随时添加和删除其中的元素。
```python
'''
python内置的一种数据类型是列表：list。list是一种有序的集合，
可以随时添加和删除其中的元素。

len():获取list元素的个数
用索引来访问list中每一个位置的元素，记得索引是从0开始的：
append(el) 追加元素
insert(i,el) 把元素插入到指定位置
pop(): 删除list末尾元素
pop(i): 删除指定位置的元素
'''
sex = ['男','女']
print(sex)
print('-------')
for item in sex:
    print(item)
print('-------')

sex.append('不男不女')
sex.pop()
sex.insert(0,'不男不女')
sex.pop(0)
print('-------')
for item in sex:
    print(item)
print('-------')
```

##### tuple
tuple（元组）: 有序列表。tuple和list非常类似,但是tuple一旦初始化就不能修改
```python
'''
tuple 一旦初始化之后不可修改
tuple的陷阱：当你定义一个tuple时，在定义的时候，tuple的元素就必须被确定下来
不可变的tuple因为不可变，代码更安全
'''
sex = ('男','女')
print(sex)

```