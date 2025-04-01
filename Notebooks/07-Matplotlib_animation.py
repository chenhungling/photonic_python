"""
Simulate a traveling wave in the medium of complex refractive index n + jk.

Matplotlib animation:
https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FuncAnimation.html#matplotlib.animation.FuncAnimation
https://jakevdp.github.io/blog/2012/08/18/matplotlib-animation-tutorial/

@author: Hung-Ling
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

## First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure(figsize=(5,4))
ax = plt.axes(xlim=(0,5), ylim=(-1.2,1.2))
ax.set(xlabel="X (a.u.)", ylabel="Amplitude")
ax.grid("on")
line, = ax.plot([], [], lw=2)  # ax.plot returns a list of matplotlib.lines.Line2D
fig.tight_layout()

## Animation function
## This is called sequentially
def animate(i):
    ## One can try to modify wavelength, n, c to see different wave property
    wavelength = 2.0  # Wavelength in free space (vaccum)
    n = 2 + 0.1j  # Complex refractive index of the medium
    c = 4.0  # Speed of wave in vaccum
    
    dt = 25  # Time interval between two frames in milisecond
    x = np.linspace(0,5,400)
    k = 2*np.pi * n / wavelength  # Complex wavenumber
    omega = 2*np.pi*c / wavelength  # Angular frequency
    y = np.real(np.exp(1j*(k*x - omega*i*dt/1000)))
    line.set_data(x, y)
    return line,

## Call the animator
## frames: source of data passed to func at each frame of the animation
## interval: delay between frames in milliseconds
## blit=True means only re-draw the parts that have changed
anim = animation.FuncAnimation(fig, animate, frames=200, interval=25,
                               repeat=False, blit=True)  # 5s animation in total

plt.show()
## Save the animation as a video file
# anim.save('traveling_wave.mp4', writer='ffmpeg', fps=40)
# anim.save('traveling_wave.gif', writer='pillow', fps=40)