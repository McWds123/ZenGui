import datetime
import inspect


def OL(content):
    print(f"[Log]({datetime.datetime.now()}):{content}")
def OE(content):
    print(f"[Error]({datetime.datetime.now()}):{content}")
def typeEOE(type1,type2,Parameter):
    stack = inspect.stack()
    caller_func_name = stack[1].function
    expected_type = type1.__name__
    actual_type = type(type2).__name__
    OE(f"类型错误 {Parameter}应为{expected_type} 但是 {Parameter} 实际为{actual_type}[报错位置：函数 {caller_func_name}()]")