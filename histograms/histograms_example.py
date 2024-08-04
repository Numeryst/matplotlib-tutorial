import numpy as np
import matplotlib.pyplot as plt

# Generate random data for the 2D histogram
x = np.random.randn(10000)
y = np.random.randn(10000)

# Create a figure and axis with the specified background color
fig, ax = plt.subplots()
fig.patch.set_facecolor("#1D1E23")
ax.set_facecolor("#1D1E23")

# Plot the 2D histogram
hist = ax.hist2d(x, y, bins=50, cmap="viridis")

# Add a colorbar with custom settings to ensure good contrast
cbar = plt.colorbar(hist[3], ax=ax)
cbar.set_label("Counts")
cbar.outline.set_edgecolor("white")

# Customize the plot to enhance visibility
ax.tick_params(colors="white")
ax.spines["top"].set_color("white")
ax.spines["right"].set_color("white")
ax.spines["bottom"].set_color("white")
ax.spines["left"].set_color("white")
ax.xaxis.label.set_color("white")
ax.yaxis.label.set_color("white")
ax.title.set_color("white")

# Add labels and a title
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_title("2D Histogram with Custom Background Color")

# Display the plot
plt.show()
