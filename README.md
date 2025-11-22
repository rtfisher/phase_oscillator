# Phase Oscillator

A Python script for visualizing the phase response of a forced damped harmonic oscillator, comparing lag and lead phase conventions.

## Overview

This script plots the phase shift between the driving force and the displacement of a damped harmonic oscillator as a function of the driving frequency. It demonstrates the difference between two common phase conventions used in physics:

- **Lag convention**: Phase shift of displacement relative to driving force (positive when displacement lags)
- **Lead convention**: Phase shift of driving force relative to displacement (negative of lag convention)

## Physics Background

For a forced damped harmonic oscillator governed by:

```
mẍ + 2βmẋ + mω₀²x = F₀cos(ωt)
```

The steady-state solution has a phase shift φ relative to the driving force:

```
φ_lag = arctan(2βω / (ω₀² - ω²))
```

Key features of the phase response:
- At low frequencies (ω << ω₀): phase ≈ 0 (in phase)
- At resonance (ω = ω₀): phase = ±π/2
- At high frequencies (ω >> ω₀): phase ≈ ±π (out of phase)

## Requirements

- Python 3.x
- NumPy
- Matplotlib

Install dependencies:
```bash
pip install numpy matplotlib
```

## Usage

Simply run the script:
```bash
python phase_oscillator.py
```

This will display a plot showing the phase response for both lag and lead conventions.

## Customization

You can modify the following parameters in the script:

### Physical Parameters
- `beta`: Damping parameter (default: 0.2) - This controls the width and shape of the phase transition

### Frequency Range
- Modify line 9 to change the frequency range:
  ```python
  omega = np.linspace(0.001, 5*omega0, 2000)
  ```
  - First argument: minimum frequency
  - Second argument: maximum frequency
  - Third argument: number of points

### Plot Appearance
- Figure size: Modify `figsize` parameter in line 16
- Line colors and styles: Modify `color`, `lw`, and `linestyle` parameters in lines 17-18
- Plot title and labels: Modify strings in lines 27-29

## Example Output

The plot shows:
- Blue solid line: Lead convention (negative phase)
- Dashed line: Lag convention (positive phase)
- Red vertical line: Resonance frequency (ω = ω₀)
- Gray horizontal lines: ±π/2 reference lines
- Black horizontal line: Zero phase reference

## Understanding the Plot

- **Below resonance** (ω/ω₀ < 1): The displacement is nearly in phase with the driving force
- **At resonance** (ω/ω₀ = 1): The displacement lags the force by exactly π/2 (90°)
- **Above resonance** (ω/ω₀ > 1): The displacement approaches π phase difference (180°, opposite phase)

The choice between lag and lead convention is a matter of preference; both contain the same physical information but with opposite sign conventions.

## License

This code is provided for educational purposes.

## Author

Generated for PHY313 course materials.
