# Python函数入门教程

## 项目概述
这是一个Python函数基础教学项目，从最基础的函数概念开始，帮助初学者理解Python函数的定义和使用方法。

## 什么是函数？
函数是Python中一个重要的概念，它就像是一个可以重复使用的代码块。我们可以把它想象成一个工具箱里的工具，每次需要的时候就可以拿出来用。

## def关键字详解
### 1. def的作用
`def` 是Python中用来定义函数的关键字（keyword）。当你看到 `def` 时，就知道这里要创建一个新的函数了。

### 2. 基本语法结构
```python
def say_hello():
    """
    这是一个简单的打招呼函数
    不需要参数
    直接打印"你好！"
    """
    print("你好！")
```

### 3. 函数定义的组成部分
1. **def关键字**：告诉Python"我要定义一个函数"
2. **函数名**：比如`say_hello`，是这个函数的名字
3. **参数括号**：`()`用来放置参数，可以为空
4. **冒号**：`:`表示函数定义的开始
5. **函数体**：缩进的代码块，是函数的具体内容

### 4. 函数文档
函数文档（docstring）是用三个引号括起来的文字说明：
```python
"""
这是函数的说明文档
可以写多行
用来解释函数的用途
"""
```

### 5. 调用函数
定义函数后，使用函数名加括号就可以调用这个函数：
```python
say_hello()  # 输出：你好！
```

## 函数的基本特点
1. **可重复使用**：
   - 函数一旦定义，可以多次调用
   - 避免重复写同样的代码

2. **代码组织**：
   - 让代码更有条理
   - 便于维护和修改

3. **命名规则**：
   - 使用小写字母
   - 单词之间用下划线连接
   - 名字要能表达函数的功能

## 练习建议
1. **基础练习**：
   - 修改say_hello函数，让它打印不同的问候语
   - 尝试定义一个不带参数的新函数

2. **观察练习**：
   - 运行代码，观察函数的执行过程
   - 注意函数定义和调用的区别

## 常见问题
1. **为什么要用函数？**
   - 代码复用
   - 使程序更有条理
   - 便于维护

2. **函数定义和调用的区别？**
   - 定义：创建函数（用def）
   - 调用：使用函数（函数名加括号）

## 下一步学习建议
1. 学习带参数的函数
2. 了解函数的返回值
3. 探索更复杂的函数应用

记住：函数就像是一个工具，定义函数就是制造工具，调用函数就是使用工具。多练习、多实验是掌握函数的最好方法！

# Python函数进阶教程

## 函数参数详解

### 1. 什么是函数参数？
函数参数是我们传递给函数的值，使函数能够处理不同的数据。就像给工具提供不同的原材料。

### 2. 参数的类型
1. **基本参数**
   ```python
   def say_hello(name):
       print(f"你好，{name}！")
   ```
   - 必须提供参数
   - 按位置传递

2. **默认参数**
   ```python
   def print_info(name, age=18):
       print(f"姓名：{name}, 年龄：{age}")
   ```
   - 有默认值的参数
   - 可以不传递，使用默认值

### 3. 参数的使用方法
1. **位置参数调用**
   ```python
   result = calculate_sum(5, 3)
   ```

2. **关键字参数调用**
   ```python
   print_info(name="小明", age=20)
   ```

3. **混合使用**
   ```python
   print_info("小明", age=20)
   ```

### 4. 函数返回值
- 使用`return`语句返回结果
- 可以返回任何类型的数据
- 如果没有return语句，默认返回None

## 练习建议
1. **基础练习**
   - 修改say_hello函数，让它能问候多个人
   - 为calculate_sum函数添加更多参数

2. **进阶练习**
   - 创建一个函数，既能加法也能减法
   - 添加参数类型检查

## 注意事项
1. 参数命名要有意义
2. 默认参数要放在普通参数后面
3. 注意参数的数量和类型

## 下一步学习建议
1. 学习*args和**kwargs的使用
2. 了解函数的作用域
3. 探索更多参数的使用方式

记住：参数使函数更灵活，但也要注意不要设置太多参数，保持函数的简单明了。
