#闭包函数：在一个函数内部定义了另外一个函数，内部的函数可用外部函数的变量
#并且外部函数的返回值是内部函数的索引
#当外部函数退出时会为内部函数保留局部变量值，以供再次调用时使用
def createCounter():
    i=0
    def counter():
        nonlocal i
        i=i+1
        return i
    return counter
	