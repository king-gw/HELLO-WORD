#第一种错误类型
a = 3
b = 2
assert b < a
#第二种错误类型
try:
    1/0
    info = {'name':'koby','age':'38'}
    print(info[name1])#名字没有定义
    print(info['info'])#键错误。对比上面的方法
    print(info[name])#名字没有被定义
    print(info['name'])#正确的输入方法
except ZeroDivisionError:
    print('除数不能为零')
except KeyError:
    print('键错误')
except NameError:
    print('名字错误，没有定义')
print('保存之后还能继续运行以下的代码')
#第三种错误类型
try:
    1/0
    info = {'name':'koby','age':'38'}
    print(info[name1])#名字没有定义
    # print(info['info'])#键错误。对比上面的方法
    # print(info[name])#名字没有被定义
    # print(info['name'])#正确的输入方法
except ZeroDivisionError as e:
    print(e)
    print('除数不能为零')
except KeyError as e:
    print(e)
    print('键错误')
except NameError as e:
    print(e)
    print('名字错误，没有定义')
print('保存之后还能继续运行以下的代码')
#第四种错误类型
try:
#    1/0
    info = {'name':'koby','age':'38'}
    print(info[name1])#名字没有定义
    print(info['info'])#键错误。对比上面的方法
    print(info[name])#名字没有被定义
    print(info['name'])#正确的输入方法
except (ZeroDivisionError,KeyError,NameError) as e:
    print(e)
    print('有错啦')
#第五种错误类型
try:
#    1/0
    info = {'name': 'koby', 'age': '38'}
#    print(info[name1])  # 名字没有定义
#    print(info['info'])  # 键错误。对比上面的方法
#    print(info[name])  # 名字没有被定义
    print(info['name'])  # 正确的输入方法
except:          #接受所有错误，，，对比if和else的用法，感觉有相似的地方
    print('有错啦')
else:
    print('没有错误')
#以上的总结
while True:
    a = int(input('请输入第一个数字：'))
    b = int(input('请输入第二个数字：'))
    try:
        print(int(a/b))
        print(a/b)#默认为浮点型，因为两整数相处可能出现浮点类型
    except ZeroDivisionError as e:
        print(e)
        print('除数不能为零')
        continue
    else:
        break
print('完成！')
#第六种错误类型
try:
    1/0
    info = {'name':'koby','age':'38'}
    print(info[name1])#名字没有定义
    # print(info['info'])#键错误。对比上面的方法
    # print(info[name])#名字没有被定义
    # print(info['name'])#正确的输入方法
except ZeroDivisionError as e:
    print(e)
    print('除数不能为零')
except KeyError as e:
    print(e)
    print('键错误')
except NameError as e:
    print(e)
    print('名字错误，没有定义')
finally:                      #任何错误都会输出，并不会报错
    print('不管如何都会运行')
print('保存之后还能继续运行以下的代码')
# 第七种错误类型
try:
    1/0
    info = {'name':'koby','age':'38'}
    print(info[name1])#名字没有定义
    # print(info['info'])#键错误。对比上面的方法
    # print(info[name])#名字没有被定义
    # print(info['name'])#正确的输入方法
except ZeroDivisionError as e:
    print(e)
    print('除数不能为零')
#    raise #抛出错误类型，也就是报错的内容。
    raise ZeroDivisionError('指定的方式输出报错内容')
except KeyError as e:
    print(e)
    print('键错误')
except NameError as e:
    print(e)
    print('名字错误，没有定义')
finally:                      #任何错误都会输出，并不会报错
    print('不管如何都会运行')
print('保存之后还能继续运行以下的代码')
#自定义错误类型
class ABCDEFG(Exception):
    def __init__(self,arg):
        self.arg = arg

    def __str__(self):
        return self.arg

try:
    print('fhgbiue')
    raise ABCDEFG('自定义的错误，现实并不存在')
except ABCDEFG as e:
    print(e)
    print('不存在的错误类型')
#    raise ABCDEFG('laalalal')
#    raise