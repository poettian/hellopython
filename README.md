# 复合结构
list、tuple、dict、set

# 函数
**位置参数**

`def power(x)`

**默认参数**

`def power(x, n=2)`

**可变参数**

`def calc(*numbers)`

**关键字参数**

`def person(name, age, **kw)`

**命名关键字参数**

`def person(name, age, *, city, job)`

`def person(name, age, *args, city, job)`

在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。

对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的。

# 高级特性
切片、循环、列表生成式、生成器

凡是可作用于for循环的对象都是Iterable类型；

凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；

# 函数式编程
高阶函数：[map,reduce,filter,sorted]

闭包

匿名函数(lambda)

装饰器

```python
import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper
  
@log
def now():
    print('2024-6-1')
```

偏函数

`functools.partial(func, /, *args, **keywords)`

# 模块

包和模块。

每一个包目录下面都会有一个`__init__.py`的文件，这个文件是必须存在的，否则，Python就把这个目录当成普通目录，而不是一个包。`__init__.py`可以是空文件，也可以有Python代码，因为`__init__.py`本身就是一个模块，而它的模块名就是`mycompany`。

包可以多级：

```python
mycompany
 ├─ web
 │  ├─ __init__.py
 │  ├─ utils.py
 │  └─ www.py
 ├─ __init__.py
 ├─ abc.py
 └─ utils.py
```

模块的标准文件模板：

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'Michael Liao' # 任何模块代码的第一个字符串都被视为模块的文档注释。

import sys

def test():
    args = sys.argv
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

# 当我们在命令行运行hello模块文件时，Python解释器把一个特殊变量__name__置为__main__，而如果在其他地方导入该hello模块时，if判断将失败
# 因此，这种if测试可以让一个模块通过命令行运行时执行一些额外的代码，最常见的就是运行测试。
if __name__=='__main__': 
    test()
```

默认情况下，Python解释器会搜索当前目录、所有已安装的内置模块和第三方模块，搜索路径存放在`sys`模块的`path`变量中。

# 面向对象编程

类名通常是大写开头的单词，创建实例是通过类名+()实现的。

注意到`__init__`方法的第一个参数永远是`self`，表示创建的实例本身。

如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线`__`，在Python中，实例的变量名如果以`__`开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问。

使用 `@property` 给属性添加 getter 和 setter 方法。

允许多重继承，提到了 MixIn 模式。

提到了多个魔术方法：`__slots__` `__len__` `__str__` `__repr__` `__iter__` `__getitem__` `__getattr__` `__call__` 。

介绍了枚举类：

```python
from enum import Enum

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
```

# 错误、调试和测试

捕获异常： `try...except...finally...` 注意是 except，命名有点奇怪。

抛出异常：`raise` 。

错误类型和继承关系见：https://docs.python.org/3/library/exceptions.html#exception-hierarchy

可以使用 pdb 调试代码。

编写单元测试时，我们需要编写一个测试类，从`unittest.TestCase`继承。

以`test`开头的方法就是测试方法，不以`test`开头的方法不被认为是测试方法，测试的时候不会被执行。

使用 `doctest` 执行文档测试。

