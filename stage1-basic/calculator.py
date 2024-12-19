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
