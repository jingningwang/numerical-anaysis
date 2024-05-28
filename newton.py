import numpy as np
#函数f(x)
def f(x):
    '''
    :param x: np.array
    :return: np.array, f(x)
    '''
    return 3*x**3-10*x**2+5*x+1 #返回向量化运算结果
#导函数f'(x)
def df(x):
    '''
        :param x: np.array
        :return: np.array, f'(x)
        '''
    return 9*x**2-20*x+5


#牛顿法求根
def Newton(x0,eta):
    '''
    :param a: 有根区间[a, b]
    :param b:
    :param epsilon: 误差1
    :param eta: 误差2 |f(x)| <eta
    :param N: 最大迭代次数
    :return: x_1, 牛顿法所求的根
    '''
    n = 0 #迭代次数计数器
    # print(f'牛顿法第{n}次迭代值为x = {x1}')
    while abs(f(x0)) > eta :
        x1 = x0 - f(x0)/df(x0)
        x0 = x1
        n += 1
        print(f'牛顿法第{n}次迭代值为x = {x1}')
    print('---' * 10)
    print(f'牛顿法迭代 {n} 次求得方程的根为 x* = {x1}')
    return x1

if __name__ == '__main__':
    x0 = 2.5 #迭代初始值
    # epsilon = 0.05  # 精度1
    eta = 0.05   #精度2
    # N = 100          #最大迭代次数
    Newton(x0=x0, eta=eta)