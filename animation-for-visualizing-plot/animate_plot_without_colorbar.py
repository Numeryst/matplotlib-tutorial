import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


# Define the function to plot
def f(x, y):
    return np.sin(np.sqrt(x**2 + y**2))


# Set up the grid in the x and y dimensions
x = np.linspace(-30, 30, 200)
y = np.linspace(-30, 30, 200)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

# Create a figure and axis
fig, ax = plt.subplots(facecolor="black")
ax.set_facecolor("black")

# Initial plot
heatmap = ax.imshow(
    Z,
    # cmap="viridis",
    # cmap="inferno",
    cmap="jet",
    # cmap="magma",
    # cmap="cividis",
    origin="lower",
    extent=(float(np.min(x)), float(np.max(y)), float(np.min(x)), float(np.max(y))),
)
# ax.set_xlim(-100, 100)
# ax.set_ylim(-100, 100)


# Function to update the plot
def update(frame):
    Z = f(
        X - frame / 10.0,
        Y + frame / 10.0,
    )  # Modify y with the frame number for animation
    heatmap.set_data(Z)
    return [heatmap]


# Create animation
anim = FuncAnimation(fig, update, frames=np.arange(0, 400, 1), interval=25, blit=False)

# anim.save("heatmap.gif")
# Show the plot
plt.show()
