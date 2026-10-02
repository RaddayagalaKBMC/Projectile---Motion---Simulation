import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math

u = 50        
theta_deg = 45  
g = 9.81      

theta = math.radians(theta_deg)

T_flight = (2 * u * math.sin(theta)) / g
H = (u**2 * (math.sin(theta))**2) / (2 * g)
R = (u**2 * math.sin(2 * theta)) / g

t = np.linspace(0, T_flight, num=100)

x = u * math.cos(theta) * t
y = (u * math.sin(theta) * t) - (0.5 * g * t**2)

fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(-10, R + 15)
ax.set_ylim(-10, H + 15)
ax.set_title('Projectile Motion: General Case', fontsize=14, fontweight='bold')

ax.set_xticks([])
ax.set_yticks([])

ax.axhline(0, color='black', linewidth=1)
ax.axvline(0, color='black', linewidth=1)

ax.text(-3, -4, '0', fontsize=12)
ax.text(R, -6, r'$R$', fontsize=14, ha='center', color='black')
ax.annotate('', xy=(R, -2), xytext=(0, -2), arrowprops=dict(arrowstyle='<->', color='black', lw=1.5))

ax.plot([R/2, R/2], [0, H], 'k--', alpha=0.5)
ax.text(R/2 + 3, H/2, r'$h$', fontsize=14, color='black')

eq_text = (
    r"$h = \frac{u^2 \sin^2 \theta}{2g}$" + "\n\n" +
    r"$t = \frac{u \sin \theta}{g}$" + "\n\n" +
    r"$T = \frac{2u \sin \theta}{g}$" + "\n\n" +
    r"$R = \frac{u^2 \sin 2\theta}{g}$"
)
ax.text(0.02, 0.95, eq_text, transform=ax.transAxes, fontsize=14, va='top',
        bbox=dict(boxstyle='round', facecolor='white', edgecolor='gray', alpha=0.8, pad=0.8))

line, = ax.plot([], [], color='blue', linewidth=2, label='Trajectory') 
point, = ax.plot([], [], 'ro', markersize=8) 

quiver_v = ax.quiver(0, 0, 0, 0, color='green', angles='xy', scale_units='xy', scale=1.5, width=0.004, label=r'$v$ (Resultant)')
quiver_vx = ax.quiver(0, 0, 0, 0, color='red', angles='xy', scale_units='xy', scale=1.5, width=0.004, label=r'$v_x = u \cos(\theta)$')
quiver_vy = ax.quiver(0, 0, 0, 0, color='orange', angles='xy', scale_units='xy', scale=1.5, width=0.004, label=r'$v_y = u \sin(\theta) - gt$')

ax.legend(loc='upper right', fontsize=11)

def update(frame):
    line.set_data(x[:frame], y[:frame])
    current_x = x[frame]
    current_y = y[frame]
    point.set_data([current_x], [current_y])
    
    vx = u * math.cos(theta)
    vy = u * math.sin(theta) - g * t[frame]
    
    quiver_v.set_offsets([[current_x, current_y]])
    quiver_v.set_UVC(vx, vy)
    
    quiver_vx.set_offsets([[current_x, current_y]])
    quiver_vx.set_UVC(vx, 0)
    
    quiver_vy.set_offsets([[current_x, current_y]])
    quiver_vy.set_UVC(0, vy)
    
    return line, point, quiver_v, quiver_vx, quiver_vy

ani = animation.FuncAnimation(fig, update, frames=len(t), interval=50, blit=False, repeat=True)

plt.show()