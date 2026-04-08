from data_gen import generate_ev_waveforms
from features import get_power_quality_metrics
from model import PFCController
import numpy as np
import matplotlib.pyplot as plt

# 1. Data Collection
print("Starting Research Simulation...")
X, y = [], []
agent = PFCController()

for _ in range(2000):
    _, v, i = generate_ev_waveforms()
    pf, thd = get_power_quality_metrics(v, i)
    # Target: The duty cycle required to fix the PF (Simulated ground truth)
    target = 0.4 + (0.4 * (1 - pf)) 
    X.append([pf, thd])
    y.append(target)

# 2. Training
agent.fit(np.array(X), np.array(y))
print("Model trained. Validating results...")

# 3. Final Test & Visualization
t, v, i_dirty = generate_ev_waveforms()
pf_in, thd_in = get_power_quality_metrics(v, i_dirty)
duty_out = agent.predict([pf_in, thd_in])

print(f"Results: Input PF: {pf_in:.2f} | Predicted Correction Duty: {duty_out:.4f}")
print("Check your folder for 'results.png'!")

# Plotting the 'Research proof'
plt.figure(figsize=(10, 4))
plt.plot(t, v/max(v), label="Voltage (Normalized)")
plt.plot(t, i_dirty/max(i_dirty), label="Current (Distorted)", linestyle='--')
plt.title(f"EV Power Analysis | PF: {pf_in:.2f}")
plt.legend()
plt.savefig("results.png")