### 变量
在程序设计中，变量是一种存储数据的载体。计算机中的变量是实际存在的数据或者说是存储器中存储数据的一块内存空间，变量的值可以被读取和修改，这是所有计算和控制的基础。计算机能处理的数据有很多中类型，除了数值之外还可以处理文本、图形、音频、视频等各种各样的数据，那么不同的数据就需要定义不同的存储类型。Python中的数据类型很多，而且也允许我们自定义新的数据类型（这一点在后面会讲到），我们先介绍几种常用的数据类型。
1. 整型(int)
2. 浮点型(float)
3. 字符串(str)
4. 布尔型(bool)(True,False)
5. 复合型

在对变量类型进行转换时可以使用Python的内置函数：
+ int(): 将一个数值或字符串转换成整数，可以指定进制。
+ float():将一个字符串转换成浮点数。
+ str():将指定的对象转换程字符串形式，可以指定编码。
+ chr():将整数转换程该编码对应的字符串(一个字符)。
+ ord():将字符串（一个字符）转换程杜英的编码（整数）