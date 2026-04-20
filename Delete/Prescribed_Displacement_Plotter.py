# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 00:10:11 2026

@author: aakas
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 14:06:00 2026
@author: aakas
"""
import numpy as np
import matplotlib.pyplot as plt

# Define time array
time = np.linspace(0, 95, 1000)

# Motion parameters based on your plot
amplitude = 0.017
frequency = 0.125  # 1 cycle per 8 seconds
rampup_time = 7.32

# Base sinusoidal motion
displacement = amplitude * np.sin(2 * np.pi * frequency * time)

# Apply the exact ramp-up logic from the Kratos snippet
ramp_mask = time < rampup_time
displacement[ramp_mask] *= 0.5 * (np.cos(np.pi * (1 - (time[ramp_mask] / rampup_time))) + 1)

# Create the plot
plt.figure(figsize=(15, 3), dpi=150)  # Wide aspect ratio
plt.plot(time, displacement, color='#1F4E79', linewidth=1.5, label='Prescribed Displacement')

# Configure axes and gridlines
plt.xlim(-5, 95)
plt.ylim(-0.019, 0.019)
plt.axhline(0, color='#7fb3d5', linestyle='--', linewidth=1)  # light blue dashed x-axis
plt.xticks(np.arange(0, 100, 5))
plt.yticks([-0.01, 0.00, 0.01])
plt.xlabel('Time [s]')
plt.ylabel('Prescribed Displacement', color='#1F4E79')
plt.title('Prescribed Displacement')
plt.legend(loc='upper right', bbox_to_anchor=(1.0, 1.15))

# Add the red vertical lines connecting the curve to the x-axis at specified points
targets = [32, 34, 36, 38]
for x in targets:
    # Find the exact y-value on the curve for the given x
    y_on_curve = np.interp(x, time, displacement)
   
    # Plot a vertical line from (x, 0) to (x, y_on_curve)
    plt.plot([x, x], [0, y_on_curve], color='red', linewidth=1.5)

# === NEW: Mark the points where the vertical lines meet the x-axis ===
plt.scatter(
    targets, 
    [0] * len(targets), 
    color='red', 
    marker='o', 
    s=60,           # size of the marker
    zorder=5,       # draw on top of everything
    #edgecolors='black',
    linewidths=1.5
)

# Adjust layout and show
plt.tight_layout()
plt.show()