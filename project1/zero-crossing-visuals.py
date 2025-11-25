import numpy as np
import matplotlib.pyplot as plt
from IPython.display import display

# ---------------------------------------------
# GIVEN PARAMETERS
# ---------------------------------------------
Ym = 5                     # Maximum amplitude of the sine waves
omega = 100 * np.pi       # Angular frequency (rad/s)
theta = np.pi / 6         # Phase shift added to Y2

# ---------------------------------------------
# TIME AXIS FOR SIMULATION
# ---------------------------------------------
# We simulate the signals from t = 0 to t = 0.05 sec
# The resolution is very high (100,000 samples) for accuracy.
t = np.linspace(0, 0.05, 100000)

# ---------------------------------------------
# GENERATING THE TWO SIGNALS
# ---------------------------------------------
# Y1 is the standard sine wave with no phase shift
Y1 = Ym * np.sin(omega * t)

# Y2 is phase-shifted by theta
Y2 = Ym * np.sin(omega * t + theta)


# ---------------------------------------------
# ZERO-CROSSING EXPLANATION
# ---------------------------------------------
# A zero-crossing is the point where the signal value changes sign:
#   - from positive to negative, or
#   - from negative to positive
#
# For a sine wave, zero-crossings happen each time the curve crosses the value zero.
#
# For Y2 = Ym * sin(omega*t + theta),
# the first zero-crossing gives us the earliest time where the phase-shifted signal is zero.
#
# We detect this numerically by checking where the sign of Y2 changes.
# np.sign(Y2) gives +1 for positive values, -1 for negative values.
# np.diff(...) finds where a change occurs between adjacent samples.

# ---------------------------------------------
# DETECT FIRST ZERO CROSSING
# ---------------------------------------------
zero_cross_idx = np.where(np.diff(np.sign(Y2)))[0][0]

# The actual time corresponding to that index
t_zero = t[zero_cross_idx]

print("First zero crossing of Y2 occurs at t =", t_zero, "seconds")


# ---------------------------------------------
# PLOTTING THE RESULTS
# ---------------------------------------------
plt.figure(figsize=(10, 5))

plt.plot(t, Y1, label=r"$Y_1 = Y_m \sin(\omega t)$")
plt.plot(t, Y2, label=r"$Y_2 = Y_m \sin(\omega t + \theta)$")

# Mark the zero-crossing point with a red dot
plt.scatter(t_zero, 0, color='red', label="Y2 first zero crossing")

# Plot formatting
plt.title("Effect of Phase Shift on Two Sine Waves")
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)

plt.show()