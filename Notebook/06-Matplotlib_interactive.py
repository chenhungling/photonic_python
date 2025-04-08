"""
===========
Slider Demo
===========
Using the slider widget to control visual properties of the plot.

In this example, a slider is used to choose the width a and distance d of the double slits.
You can control many continuously-varying properties of your plot in this way.
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

def calculate_intensity(theta, wavelength=0.63, a=2, d=10):
    
    k = 2*np.pi/wavelength
    E = np.cos(k*d/2*np.sin(theta))*np.sinc(k*a/2*np.sin(theta))
    intensity = np.abs(E)**2

    return intensity

L = 10  # Focal length (mm)
theta = np.linspace(-15,15,1000) * np.pi/180  # Angle in radians
X = L*np.sin(theta)  # Length on a screen
a0 = 2  # Intial slit width in µm
d0 = 20  # Initial slit separation in µm

fig, ax = plt.subplots(figsize=(5,4))
fig.subplots_adjust(bottom=0.3)  # Make some space for the sliders
line, = ax.plot(X, calculate_intensity(theta, a=a0, d=d0))
ax.set(xlabel="X (mm)", ylabel="Intensity (a.u.)")

## Create new axes
ax_color = 'lightgoldenrodyellow'
ax_width = plt.axes([0.25, 0.15, 0.6, 0.03], facecolor=ax_color)
ax_dist = plt.axes([0.25, 0.1, 0.6, 0.03], facecolor=ax_color)

## Create sliders
slider_width = Slider(ax_width, 'Width (µm)', 1, 4, valinit=a0, valstep=0.1)
slider_dist = Slider(ax_dist, 'Distance (µm)', 10, 40, valinit=d0, valstep=0.2)

def update(val):
    a = slider_width.val
    d = slider_dist.val
    line.set_ydata(calculate_intensity(theta, a=a, d=d))
    fig.canvas.draw_idle()

slider_width.on_changed(update)
slider_dist.on_changed(update)

plt.show()