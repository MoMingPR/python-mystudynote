a = '我是单独的变量a'

#封装
def function_1():
    a = 'function_1中的变量a'
    print('function_1运行成功')

class new_class1():
    a = '我是类1中的变量a'
    @classmethod
    def function_2(cls):
        print('function_2运行成功')

class new_class2():
    a = '我是类2中的变量a'
    def function_3(self):
        print('function_3运行成功')

print(a)
print(new_class1.a)
new_class1.function_2()
A = new_class2()
print(A.a)