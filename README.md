# AI-Driven Adaptive Power Factor Correction (APFC) for EV Charging Infrastructure

## 🚀 Research Overview

This project addresses power quality degradation in Electric Vehicle (EV) charging stations caused by non-linear loads. Traditional fixed-parameter correction methods often fail to adapt to dynamic grid conditions. We developed a **Physics-Informed Neural Network (PINN)** approach using **MLP Regressors** and **Signal Processing (FFT)** to dynamically optimize the Power Factor (PF) and minimize Total Harmonic Distortion (THD).

### Key Performance Metrics

| Metric                        | Baseline (Uncorrected) | AI-Optimized Result        |
| :---------------------------- | :--------------------- | :------------------------- |
| **Power Factor (PF)**         | 0.59 - 0.65            | **0.98**                   |
| **Total Harmonic Distortion** | 22.4%                  | **5.2%**                   |
| **Correction Latency**        | High (Manual/Fixed)    | **Real-time (Predictive)** |

---

## 🛠 Project Structure

```text
├── data/               # Simulated load datasets and CSV logs
├── models/             # Saved model weights and scalers
├── src/                # Modular source code
│   ├── data_gen.py     # Physics engine for waveform simulation
│   ├── features.py     # Signal processing & FFT feature extraction
│   ├── model.py        # Neural Network architecture (Scikit-Learn)
│   └── main.py         # System integration and validation script
├── results.png         # Waveform comparison visualization
└── requirements.txt    # Project dependencies
🧪 Methodology & Implementation
1. Signal Processing (FFT)
To move beyond raw data, we utilized Fast Fourier Transforms to extract the 3rd and 5th order harmonics. This allows the model to "see" the specific frequency distortions created by the EV charger's inverter.

2. Predictive Modeling
utilized an MLP Regressor with a (128, 64, 32) hidden layer architecture. The model takes PF, THD, and Load Level as inputs to predict the optimal Duty Cycle (0.4–0.8) for the APFC converter.

3. Constraints
The system includes a Battery State-of-Charge (SOC) awareness module, ensuring that the intensity of power factor correction does not introduce thermal stress to the EV battery during peak charging phases.

⚙️ Installation & Usage
1. Clone the repository:

git clone [https://github.com/YOUR_USERNAME/AI-EV-Power-Optimizer.git](https://github.com/YOUR_USERNAME/AI-EV-Power-Optimizer.git)
cd AI-EV-Power-Optimizer

2. Setup Environment (Windows PowerShell):

python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt

3. Run the Simulation:

python src/main.py

📄 License & Citations
Distributed under the MIT License. This project was developed as part of a research initiative into sustainable EV infrastructure.
```
