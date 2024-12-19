# 这是最基础的函数定义方式
def say_hello(name):
    """
    带参数的问候函数
    参数:
        name: 要问候的人的名字
    """
    print(f"你好，{name}！")

def calculate_sum(a, b):
    """
    计算两个数的和
    参数:
        a: 第一个数字
        b: 第二个数字
    返回:
        两个数字的和
    """
    result = a + b
    return result

def print_info(name, age=18):
    """
    打印个人信息的函数，带默认参数
    参数:
        name: 姓名
        age: 年龄（默认为18）
    """
    print(f"姓名：{name}, 年龄：{age}")

def calculate(a, b, operation='add'):
    """
    通用计算函数，支持多种运算
    参数:
        a: 第一个数字
        b: 第二个数字
        operation: 运算类型（'add'加法，'sub'减法，'mul'乘法，'div'除法）
    返回:
        计算结果，如果除数为0返回None
    """
    if operation == 'add':
        return a + b
    elif operation == 'sub':
        return a - b
    elif operation == 'mul':
        return a * b
    elif operation == 'div':
        if b == 0:
            print("错误：除数不能为0")
            return None
        return a / b
    else:
        print("错误：不支持的运算类型")
        return None

def greet(*names):
    """
    问候多个人的函数，演示可变参数
    参数:
        *names: 任意数量的名字
    """
    for name in names:
        print(f"你好，{name}！")

def print_person_info(**info):
    """
    打印个人信息，演示关键字参数
    参数:
        **info: 包含个人信息的字典
    """
    for key, value in info.items():
        print(f"{key}: {value}")

# 测试函数
print("\n=== 函数参数示例 ===")
# 1. 基本参数调用
say_hello("小明")

# 2. 返回值的使用
result = calculate_sum(5, 3)
print(f"5 加 3 的结果是：{result}")

# 3. 默认参数的使用
print_info("小红")  # 使用默认年龄
print_info("小张", 20)  # 指定年龄

# 测试代码
print("\n=== 函数进阶示例 ===")

# 1. 默认参数和不同运算
print("\n基本运算测试：")
print(f"10 + 5 = {calculate(10, 5)}")
print(f"10 - 5 = {calculate(10, 5, 'sub')}")
print(f"10 * 5 = {calculate(10, 5, 'mul')}")
print(f"10 / 5 = {calculate(10, 5, 'div')}")

# 2. 可变参数
print("\n问候测试：")
greet("小明", "小红", "小张")

# 3. 关键字参数
print("\n个人信息测试：")
print_person_info(name="小明", age=20, city="北京", hobby="编程")
