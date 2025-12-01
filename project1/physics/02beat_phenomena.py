import numpy as np
import matplotlib.pyplot as plt

# Parameters
A = 1
f1 = 260  # Hz
f2 = 252  # Hz
t = np.linspace(0, 3, 5000)  # 1 second, high resolution

# Beat signal
y = A * (np.sin(2 * np.pi * f1 * t) + np.sin(2 * np.pi * f2 * t))

# Plot
plt.plot(t, y)
plt.title("Beat Phenomenon: f1=260Hz, f2=252Hz")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.xlim(0, 0.1)  # Zoom in for visible beats
plt.grid(True)
plt.show()