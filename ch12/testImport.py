# -*- coding:UTF-8 -*-


# import 搜索路径  PYTHONPATH ,  sys.path
# PEP8 import 顺序
# python标准库模块
# python第三方模块
# 应用程序自定义模块

# 局部名称空间、全局名称空间、内建名称空间

# from XXX import yyy  导入到当前名空间， 可直接使用yyy
# import XXX           导入模块， 需要XXX.yyy 方式使用属性
# import XXX as   ZZZ   别名, 不想使用较长的类名时使用
from ch12 import settings as conVar
from ch12.settings import TEST_STRING

#from .settings import TEST_STRING

print(conVar.SECRET_KEY)
print(TEST_STRING)





bar = 100


def foo():
    """
     this is doc of function foo
    """
    print('calling foo()...')
    # 局部的bar覆盖了全局的bar
    bar = 200
    a = 1
    print("in foo(),bar is", bar)
    #全局名空间
    print(globals().keys())
    #局部名空间
    print(locals().keys())

print('in __main__ bar is ', bar)
foo()
print(foo.__doc__)
print(foo.__name__)

