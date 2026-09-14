import numpy as np 
import matplotlib.pyplot as plt
#generate 100 points in 2D space
x=np.random.rand(100,2)
#take x1 and x2
x1 = x[:, 0] 
x2 = x[:, 1]
#find x1^2+x2^2
distance = x1**2 + x2**2
#class 0 if distance < 1, class 1 if distance >= 1
y = []
for d in distance:
    if d < 1:
        y.append(0)
    else:
        y.append(1)
for i in range(100):
    if y[i] == 0:
        plt.scatter(x1[i], x2[i], marker="o",label="Class 0" if i == 0 else "")
    else:
        plt.scatter(x1[i], x2[i], marker="x",label="Class 1" if i == 0 else "")
circle = plt.Circle((0, 0), 1, fill=False)
plt.gca().add_patch(circle)
plt.xlabel("x1")
plt.ylabel("x2")
plt.title("100 Points with Two Classes")
plt.legend()
plt.show()