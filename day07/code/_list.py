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


