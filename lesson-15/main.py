import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# ==========================================================
# 1. Basic Plotting
# f(x) = x² - 4x + 4
# ==========================================================

x = np.linspace(-10, 10, 400)
y = x**2 - 4*x + 4

plt.figure()
plt.plot(x, y, color="blue")
plt.title("Plot of f(x) = x² - 4x + 4")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.show()


# ==========================================================
# 2. Sine and Cosine Plot
# ==========================================================

x = np.linspace(0, 2*np.pi, 200)

plt.figure()
plt.plot(x, np.sin(x), 'r--', marker='o', label="sin(x)")
plt.plot(x, np.cos(x), 'b-', marker='x', label="cos(x)")
plt.title("Sine and Cosine Functions")
plt.xlabel("x")
plt.ylabel("Value")
plt.legend()
plt.grid(True)
plt.show()


# ==========================================================
# 3. Subplots (2x2)
# ==========================================================

x = np.linspace(-2, 2, 200)

fig, axs = plt.subplots(2, 2, figsize=(10,8))

# x³
axs[0,0].plot(x, x**3, color="red")
axs[0,0].set_title("f(x) = x³")
axs[0,0].set_xlabel("x")
axs[0,0].set_ylabel("y")

# sin(x)
axs[0,1].plot(x, np.sin(x), color="blue")
axs[0,1].set_title("f(x) = sin(x)")
axs[0,1].set_xlabel("x")

# e^x
axs[1,0].plot(x, np.exp(x), color="green")
axs[1,0].set_title("f(x) = e^x")
axs[1,0].set_xlabel("x")

# log(x+1)
x_log = np.linspace(0, 5, 200)
axs[1,1].plot(x_log, np.log(x_log+1), color="purple")
axs[1,1].set_title("f(x) = log(x+1)")
axs[1,1].set_xlabel("x")

plt.tight_layout()
plt.show()


# ==========================================================
# 4. Scatter Plot
# ==========================================================

x = np.random.uniform(0, 10, 100)
y = np.random.uniform(0, 10, 100)

plt.figure()
plt.scatter(x, y, c=np.random.rand(100), marker='o')
plt.title("Random Scatter Plot")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.grid(True)
plt.show()


# ==========================================================
# 5. Histogram
# ==========================================================

data = np.random.normal(0, 1, 1000)

plt.figure()
plt.hist(data, bins=30, alpha=0.7)
plt.title("Histogram of Normal Distribution")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()


# ==========================================================
# 6. 3D Surface Plot
# f(x,y) = cos(x² + y²)
# ==========================================================

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = np.linspace(-5,5,100)
y = np.linspace(-5,5,100)

X, Y = np.meshgrid(x, y)
Z = np.cos(X**2 + Y**2)

surface = ax.plot_surface(X, Y, Z, cmap="viridis")

ax.set_title("3D Surface: cos(x² + y²)")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

fig.colorbar(surface)
plt.show()


# ==========================================================
# 7. Bar Chart
# ==========================================================

products = ['Product A','Product B','Product C','Product D','Product E']
sales = [200,150,250,175,225]

plt.figure()
plt.bar(products, sales, color=['red','blue','green','orange','purple'])
plt.title("Product Sales")
plt.xlabel("Products")
plt.ylabel("Sales")
plt.show()


# ==========================================================
# 8. Stacked Bar Chart
# ==========================================================

periods = ['T1','T2','T3','T4']

catA = np.array([5,7,6,8])
catB = np.array([3,4,5,3])
catC = np.array([4,2,3,4])

plt.figure()

plt.bar(periods, catA, label="Category A")
plt.bar(periods, catB, bottom=catA, label="Category B")
plt.bar(periods, catC, bottom=catA+catB, label="Category C")

plt.title("Stacked Category Contributions")
plt.xlabel("Time Period")
plt.ylabel("Values")
plt.legend()

plt.show()