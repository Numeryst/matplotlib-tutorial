import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters for synthetic data
num_frames = 100  # Number of frames in the animation
data_size = (10, 10)  # Size of the heatmap

# Generate synthetic data
data = np.random.rand(num_frames, data_size[0], data_size[1])

# Create a figure and axes
fig, ax = plt.subplots()
cax = ax.matshow(data[0], cmap="viridis")

# Add a colorbar
fig.colorbar(cax)


# Function to update the heatmap
def update(frame):
    cax.set_data(data[frame])
    return [cax]


# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, blit=True)

# Display the animation
plt.show()

# Save the animation
# ani.save('animated_heatmap.mp4', writer='ffmpeg')
