## 模块

我们推荐所有的模块在Python模块的开头部分导入，而且最好按照这样的顺序：
- Python标准库模块
- Python第三方模块
- 应用程序自定义模块

- 模块开头的 __all__=[], 其他地方导入后只能使用__all__ 中指定的，引用all 以外的属性会报错


- 局部名称空间、全局名称空间、内建名称空间

- from XXX import yyy  导入到当前名空间， 可直接使用yyy
- import XXX           导入模块， 需要XXX.yyy 方式使用属性
- import XXX as   ZZZ   别名, 不想使用较长的类名时使用