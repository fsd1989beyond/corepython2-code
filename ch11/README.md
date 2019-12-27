## 函数和函数式编程

### 嵌套函数
  - 第一，函数的嵌套能够保证内部函数的隐私
    ```
    def connect_DB():
        def get_DB_configuration():
        ...
        return host, username, password
    conn = connector.connect(get_DB_configuration())
    return conn
    ```
  - 第二，合理的使用函数嵌套，能够提高程序的运行效率
    ```
    def factorial(input):
        # validation check
        if not isinstance(input, int):
            raise Exception('input must be an integer.')
        if input < 0:
            raise Exception('input must be greater or equal to 0' )
        ...

        def inner_factorial(input):
            if input <= 1:
                return 1
            return input * inner_factorial(input-1)
        return inner_factorial(input)
    
    print(factorial(5))
    ```


  
- 闭包  
  闭包其实和嵌套函数类似，不同的是，这里外部函数返回的是一个函数，而不是一个具体的值。返回的函数通常赋于一个变量，这个变量可以在后面被继续执行调用。闭包常常和装饰器（decorator）一起使用 
  ```
    def nth_power(exponent):
        def exponent_of(base):
            return base ** exponent
        return exponent_of # 返回值是exponent_of函数

    square = nth_power(2) # 计算一个数的平方
    cube = nth_power(3) # 计算一个数的立方 
    square
    # 输出
    <function __main__.nth_power.<locals>.exponent(base)>

    cube
    # 输出
    <function __main__.nth_power.<locals>.exponent(base)>

    print(square(2))  # 计算2的平方
    print(cube(2)) # 计算2的立方
    # 输出
    4 # 2^2
    8 # 2^3
    ```

### 匿名函数lambda
匿名函数的格式： `lambda argument1, argument2,... argumentN : expression`
- 第一，lambda 是一个表达式（expression），并不是一个语句（statement）    
    ```
    [(lambda x: x*x)(x) for x in range(10)]
    # 输出
    [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
    ```
    ```
    l = [(1, 20), (3, 0), (9, 10), (2, -1)]
    l.sort(key=lambda x: x[1]) # 按列表中元祖的第二个元素排序
    print(l)
    # 输出
    [(2, -1), (3, 0), (9, 10), (1, 20)]
    ```
- 第二，lambda 的主体是只有一行的简单表达式，并不能扩展成一个多行的代码块。 
    `lambda 专注于简单的任务，而常规函数则负责更复杂的多行逻辑。`  
    `你需要一个函数，但它非常简短，只需要一行就能完成；同时它在程序中只被调用一次而已。`

### 函数式编程
    `所谓函数式编程，是指代码中每一块都是不可变的（immutable），都由纯函数（pure function）的形式组成。
     这里的纯函数，是指函数本身相互独立、互不影响，对于相同的输入，总会有相同的输出，没有任何副作用。`
     
     