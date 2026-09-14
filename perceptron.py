import numpy as np
x=np.array([ [1, 0], [2, 1], [1, 2], [2, 0], [3, 0] ])
y = np.array([1, 0, 0, 1, 1])
w1 = 0.3 
w2 = 0.2
eta = 0.1
theta = -1
b = 1
iteration=10
for epoch in range(iteration):
    for i in range(len(x)):
        x1=x[i][0]
        x2=x[i][1]
        target=y[i]
        z=w1*x1+w2*x2+b
        y_hat=1 if z>theta else 0
        error=target-y_hat
        delta_w1=eta*(target-y_hat)*x1
        delta_w2=eta*(target-y_hat)*x2
        delta_b=eta*(target-y_hat)
        update_w1=w1+delta_w1
        update_w2=w2+delta_w2
        update_b=b+delta_b
        w1=update_w1
        w2=update_w2
        b=update_b
        print("sample", i+1,"target:", target, "predicted:", y_hat, "error:", error, "updated weights:", w1, w2, "updated bias:", b)
    print("\final result after 10 epochs:")
    print("Final weights:", w1, w2)
    print("Final bias:", b)
    print('error:', error)
    import matplotlib.pyplot as plt
    class_0 = x[y == 0]
    class_1 = x[y == 1]
    plt.scatter(class_0[:, 0], class_0[:, 1],label='Class 0')
    plt.scatter(class_1[:, 0], class_1[:, 1],label='Class 1')
    plt.xlabel("x1")
    plt.ylabel("x2")
    plt.title("Perceptron Data")
    plt.legend()
    plt.show()
    print("Final weights:", w1, w2)