import numpy as np
from scipy.optimize import fsolve
'''
此程序用二分法求非线性方程的根
'''
#函数f(x)-------------------
def f(x):
    f=3*x**3-10*x**2+5*x+1
    return f #返回向量化运算结果

#求方程的精确解--------------
soluation = fsolve(f,[0,1])
print(soluation)
soluation=soluation[1]  
soluation = round(soluation,4)


#二分法求根-----------------
def bisection(a, b, epsilon):
    '''
    :param a: 有根区间[a, b]
    :param b:
    :param epsilon: 相对误差
    :return: x_star, 二分法所求的根
    '''
    k = 0 #二分次数计数器
    while True:
        x = (a+b)/2
        x = round(x,4)
        fv=f(x)
        fv=round(fv,4)
        relative_error = abs((x-soluation)/soluation)
        relative_error=round(relative_error,4)
        k += 1
        if relative_error < epsilon: #函数值绝对值小于精度，即为所求的根
            x_star = x
            print(f'第{k}次迭代后,迭代点为{x},函数值为{fv},相对误差为{relative_error}.达到精度，迭代结束')
            break
        elif f(a) * f(x) < 0:
            b = x
            fv=f(x)
            fv=round(fv,4)
            print(f'第{k}次迭代后,迭代点为{x},函数值为{fv},相对误差为{relative_error}.')
        elif f(x) * f(b) < 0:
            a = x
            print(f'第{k}次迭代后,迭代点为{x},函数值为{fv},相对误差为{relative_error}.')
    return x_star

if __name__ == '__main__':
    a = 0.4 #有根区间
    b = 1
    epsilon = 0.05 #精度
    bisection(a=a, b=b, epsilon=epsilon)