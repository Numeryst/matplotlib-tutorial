import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.font_manager import FontProperties

# Parameters for synthetic data
num_frames = 100  # Number of frames in the animation
data_size = (10, 10)  # Size of the heatmap

# Generate synthetic data
data = np.random.rand(num_frames, data_size[0], data_size[1])

# Create a figure and axes
fig, ax = plt.subplots(facecolor="black")
# ax.set_facecolor("black")

cax = ax.matshow(data[0], cmap="viridis")

# Add a colorbar
font_properties = FontProperties(weight="bold", size=22)
cbar = fig.colorbar(cax, orientation="vertical")
cbar.set_label("Intensity", color="white", fontproperties=font_properties)
cbar.ax.yaxis.set_tick_params(color="white", labelsize=16)
plt.setp(plt.getp(cbar.ax.axes, "yticklabels"), color="white")


# Function to update the heatmap
def update(frame):
    cax.set_data(data[frame])
    return [cax]


# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, blit=True)

# ani.save("random_animate.mp4")

# Display the animation
plt.show()

# Save the animation
# ani.save('animated_heatmap.mp4', writer='ffmpeg')
