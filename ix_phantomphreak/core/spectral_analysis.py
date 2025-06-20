"""
IX-PhantomPhreak Spectral Analysis Module

Performs advanced spectral decomposition and pattern recognition on input data streams.
Used for anomaly detection, signal enhancement, and hidden pattern extraction within IX-Gibson.
"""

import numpy as np
from scipy.signal import spectrogram

class SpectralAnalysis:
    def __init__(self, sample_rate: int = 44100):
        self.sample_rate = sample_rate

    def compute_spectrogram(self, data: np.ndarray, nperseg: int = 256, noverlap: int = 128):
        frequencies, times, Sxx = spectrogram(data, fs=self.sample_rate, nperseg=nperseg, noverlap=noverlap)
        return frequencies, times, Sxx

    def detect_anomalies(self, Sxx: np.ndarray, threshold: float = 0.5):
        # Simple anomaly detection by thresholding spectral power
        anomalies = (Sxx > threshold).astype(int)
        return anomalies

# Example usage
if __name__ == "__main__":
    import matplotlib.pyplot as plt

    # Generate sample signal with noise
    fs = 1000
    t = np.linspace(0, 1.0, fs)
    signal = np.sin(2 * np.pi * 50 * t) + 0.5 * np.random.randn(fs)

    sa = SpectralAnalysis(sample_rate=fs)
    f, times, Sxx = sa.compute_spectrogram(signal)
    anomalies = sa.detect_anomalies(Sxx, threshold=0.8)

    plt.pcolormesh(times, f, Sxx, shading='gouraud')
    plt.title("Spectrogram")
    plt.ylabel("Frequency [Hz]")
    plt.xlabel("Time [sec]")
    plt.show()
