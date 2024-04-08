def gradient_descent(n, learning_rate=1e-5, epsilon=1e-4):
    # 初始化x，可以选择不同的初始化值，这里选择n/2
    x = n/2   
    
    while True:
        # 计算函数值
        f_x = (x**2-n)**2
        # 计算梯度
        df_x = 4*(x**2-n)*x
        
        print('abs',abs(f_x))
        
        # 如果函数值小于我们设定的epsilon，就认为已经找到了解
        if abs(f_x) < epsilon:
            break

        # 梯度下降法和牛顿法更新的不同之处就体现在下面两行当中
        # 梯度下降法更新x
        x -= learning_rate * df_x
        # 使用牛顿下降法更新x
        x -=f_x/df_x
        print('x:',x)

    return x

print(gradient_descent(9))