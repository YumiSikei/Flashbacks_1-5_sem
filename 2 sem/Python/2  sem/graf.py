import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(a,b,100)
y=[]
for i in x:
    y.append(f(i))
plt.subploy(221)
plt.grid()
plt.plot(x,y,'blue')
plt.title(r'$x^2-5*x+6)$')
   
plt.subplot(222)
plt.grid()
plt.plot(x,y,'blue')
plt.title(r'$Корни$')
data=root_fx(a,b,h,eps,f)
for i in range(len(data)):
    plt.scatter(data[i],f(data[i]),color='green')
   
plt.subplot(223)
plt.grid()
plt.xlabel('x')
plt.plot(x,y,'blue')
plt.title(r'$Перегиб$')
data=root_fx(a,b,h,eps,-sin(x))
for i in range(len(data)):
    plt.scatter(data[i],f(data[i]),color='yellow')
   
plt.subplot(224)
plt.grid()
plt.plot(x,y,'blue')
plt.title('$Экстремумы$')
data=root_fx(a,b,h,eps,cos(x))
for i in range(len(data)):
    plt.scatter(data[i],f(data[i]),color='red')
