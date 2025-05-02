import numpy as np
import matplotlib.pyplot as plt

q = 1.0
m = 1.0
E = np.array([0, 0.5, 0])
B = np.array([0, 0, 1.0])
v0 = np.array([1.0, 0.0, 0.0])

dt = 0.001
t_max = 10
N = int(t_max / dt)
t = np.linspace(0, t_max, N)

pos = np.zeros((N, 3))
vel = np.zeros((N, 3))
vel[0] = v0

for i in range(1, N):
    F = q * (E + np.cross(vel[i-1], B))
    acc = F / m
    vel[i] = vel[i-1] + acc * dt
    pos[i] = pos[i-1] + vel[i] * dt

# Plot
plt.figure(figsize=(10,6))
plt.plot(pos[:,0], pos[:,1])
plt.title('Charged Particle in E×B Field (Scaled Units)')
plt.xlabel('x position')
plt.ylabel('y position')
plt.axis('equal')
plt.grid(True)
plt.show()
