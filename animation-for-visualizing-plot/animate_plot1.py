import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.font_manager import FontProperties


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
    cmap="jet",
    # cmap="viridis",
    # cmap="inferno",
    # cmap="magma",
    # cmap="cividis",
    origin="lower",
    vmin=np.min(Z),
    vmax=np.max(Z),
    extent=(float(np.min(x)), float(np.max(y)), float(np.min(x)), float(np.max(y))),
)
# ax.set_xlim(-100, 100)
# ax.set_ylim(-100, 100)

# Add color bar
font_properties = FontProperties(weight="bold", size=22)
cbar = fig.colorbar(heatmap, ax=ax, orientation="vertical")
cbar.set_label("Intensity", color="white", fontproperties=font_properties)
cbar.ax.yaxis.set_tick_params(color="white", labelsize=16)
plt.setp(plt.getp(cbar.ax.axes, "yticklabels"), color="white")


# Function to update the plot
def update(frame):
    Z = f(X - frame / 10.0, Y)  # Modify y with the frame number for animation
    heatmap.set_data(Z)
    heatmap.set_clim(vmin=np.min(Z), vmax=np.max(Z))  # Adjust color limits if needed
    cbar.update_normal(heatmap)  # Update the color bar to reflect new data

    # # Manually set color bar ticks
    # cbar.ax.set_yticks([np.min(Z), np.max(Z)])  # Set ticks at the min and max values
    # cbar.ax.set_yticklabels([f"{np.min(Z):.2f}", f"{np.max(Z):.2f}"])  # Label ticks
    # Generate intermediate tick values
    tick_values = np.linspace(
        np.min(Z), np.max(Z), num=8
    )  # Adjust `num` to change the number of ticks

    # Set color bar ticks and labels
    cbar.ax.set_yticks(tick_values)  # Set ticks at intermediate values
    cbar.ax.set_yticklabels(
        [f"{val:.2f}" for val in tick_values]
    )  # Label ticks with formatted values
    # Set tick color
    cbar.ax.yaxis.set_tick_params(color="white")  # Set tick color
    plt.setp(cbar.ax.get_yticklabels(), color="white")  # Set tick label color

    return [heatmap, cbar]


# Create animation
anim = FuncAnimation(fig, update, frames=np.arange(0, 400, 1), interval=25, blit=False)

# anim.save("heatmap2.mp4", writer="ffmpeg")
# Show the plot
plt.show()
