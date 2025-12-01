# simulating and detecting zero crossing

import numpy as np

# Given values
Ym = 5
omega = 100 * np.pi
theta = np.pi / 6

# Time axis for simulation
t = np.linspace(0, 0.05, 100000)  # high resolution

# Signals
Y1 = Ym * np.sin(omega * t)
Y2 = Ym * np.sin(omega * t + theta)

# Detect the first time Y2 crosses zero
# We find where the sign changes from + to - or - to +
zero_cross_idx = np.where(np.diff(np.sign(Y2)))[0][0]
t_zero = t[zero_cross_idx]

print("First zero crossing of Y2 occurs at t =", t_zero)