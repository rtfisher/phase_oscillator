import numpy as np
import matplotlib.pyplot as plt

# Parameters
omega0 = 1.0   # natural frequency
beta = 0.2     # damping parameter

# Frequency range
omega = np.linspace(0.001, 5*omega0, 2000)  # avoid zero for stability

# Phase definitions
phi_lag = np.arctan2(2*beta*omega, omega0**2 - omega**2)   # lag convention
phi_lead = -phi_lag                                        # lead convention

# Plot
plt.figure(figsize=(8,6))
plt.plot(omega/omega0, phi_lead, lw=2, color='blue', label='Lead convention')
plt.plot(omega/omega0, phi_lag, lw=2, linestyle='--', label='Lag convention')

# Reference lines
plt.axhline(0, linestyle=':', color='black')
plt.axvline(1, linestyle='--', color='red', label=r'$\omega = \omega_0$')
plt.axhline(np.pi/2, linestyle='--', linewidth=1, color='gray')
plt.axhline(-np.pi/2, linestyle='--', linewidth=1, color='gray')

# Labels and title
plt.title("Phase of Forced Damped Oscillator: Lag vs Lead", fontsize=14)
plt.xlabel(r'$\omega / \omega_0$', fontsize=12)
plt.ylabel(r'Phase $\phi$ (radians)', fontsize=12)
plt.legend()
plt.grid(True)
plt.show()

