x0 = 0.4  #区间下限
x1 = 1  #区间上限

x_list = [x1]
i = 0

def f(x):
    f = 3*x**3-10*x**2+5*x+1
    return f

while True:
    x2 = x1 - f(x1)*(x1-x0)/(f(x1)-f(x0))
    x1 = x2
    x_list.append(x2)
    if len(x_list) > 1:
        i += 1
        error = abs((x_list[-1] - x_list[-2]) / x_list[-1])
        if error < 0.05:
            print(f'迭代第{i}次后，误差小于0.05')
            break
    else:
        pass
print(x_list)
print(f'所求方程式的根为{x_list[-1]}')
