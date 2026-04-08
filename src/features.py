import numpy as np
from scipy.integrate import trapezoid

def get_power_quality_metrics(v, i):
    # Calculate Real Power Factor
    p_inst = v * i
    p_act = trapezoid(p_inst) / len(v)
    v_rms, i_rms = np.sqrt(np.mean(v**2)), np.sqrt(np.mean(i**2))
    pf = p_act / (v_rms * i_rms) if (v_rms * i_rms) != 0 else 0
    
    # Calculate THD using Fast Fourier Transform (FFT)
    fft_vals = np.abs(np.fft.fft(i))
    fundamental = fft_vals[1]
    harmonics = np.sqrt(np.sum(fft_vals[2:10]**2))
    thd = harmonics / fundamental if fundamental != 0 else 0
    
    return pf, thd