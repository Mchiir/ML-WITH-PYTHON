import numpy as np
import matplotlib.pyplot as plt

# Parameters
phi = 0
xm = -1j
omega = 2 * np.pi  # rad/s

# Time array
t = np.linspace(0, 2, 500)  # two seconds

# Signal
x = xm * np.cos(omega * t + phi)

# Parts
x_real = np.real(x)
x_imag = np.imag(x)
x_mag = np.abs(x)

# Plot
plt.figure(figsize=(10,6))
plt.plot(t, x_real, label='Re{x(t)}', linestyle='--')
plt.plot(t, x_imag, label='Im{x(t)}')
plt.plot(t, x_mag, label='|x(t)|', linestyle=':')

plt.title("Harmonic Motion with Complex Amplitude (xm = -i)")
plt.xlabel("Time [s]")
plt.ylabel("x(t)")
plt.legend()
plt.grid(True)
plt.show()