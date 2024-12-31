# 复合结构
list tuple dict set

# 函数
**位置参数**

def power(x)

**默认参数**

def power(x, n=2)

**可变参数**

def calc(*numbers)

**关键字参数**

def person(name, age, **kw)

**命名关键字参数**

def person(name, age, *, city, job)

def person(name, age, *args, city, job)

在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。

对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的。

# 高级特性
[切片,循环,列表生成式,生成器,]

凡是可作用于for循环的对象都是Iterable类型；

凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；

# 函数式编程
高阶函数：[map,reduce,]
