"""
创建一个set,需要提供一list作为输入集合
重复元素在set中会被自动过滤
通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果
通过remove(key)方法可以删除元素

set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作：
set和dict的唯一区别仅在于没有存储对应的value，但是，set的原理和dict一样，所以，同样不可以放入可变对象，
因为无法判断两个可变对象是否相等，也就无法保证set内部“不会有重复元素”
"""
s = set([1,2,3])
print(s)
s = set([1,1,1,2,2,3,4,5,5])
s.add('2')
print(s)
s.remove('2')
print(s)

s1 = set([1,2,3])
s2 = set([2,3,4])
print(s1 & s2)
print(s1 | s2)