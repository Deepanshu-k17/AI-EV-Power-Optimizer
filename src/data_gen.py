import numpy as np

def generate_ev_waveforms(samples=1000):
    t = np.linspace(0, 0.02, samples)  # 20ms window (50Hz)
    voltage = 325 * np.sin(2 * np.pi * 50 * t)  # 230V RMS
    
    # Phase shift between 20 and 60 degrees
    shift = np.radians(np.random.uniform(20, 60))
    
    # Fundamental + 3rd and 5th harmonics (Research standard)
    current = 15 * (
        0.85 * np.sin(2 * np.pi * 50 * t + shift) + 
        0.10 * np.sin(3 * 2 * np.pi * 50 * t + shift) +
        0.05 * np.sin(5 * 2 * np.pi * 50 * t + shift)
    )
    return t, voltage, current