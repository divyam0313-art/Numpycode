import matplotlib.pyplot as plt
import numpy as np

## pyplot is used for 1D plotting

x=np.linspace(1,2*np.pi ,100)
y=np.sin(x)

# print(x)

# print(np.pi)
# print("sin is", y)

plt.figure(figsize=(3,4),facecolor="limegreen",edgecolor="green")
plt.plot(x,y,label="sin(x)" , color="blue" , linestyle=":" , linewidth=2)
plt.title("Lineplot of Sine wave")
plt.xlabel("X value")
plt.ylabel("sin(x)" ,color="red",fontsize=58)
plt.legend()
plt.grid(True)
plt.show()

