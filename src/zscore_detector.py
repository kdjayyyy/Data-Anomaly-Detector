import numpy as np
from streamad.model import ZScoreDetector

class ZScoreAnomalyDetector:
    def __init__(self, window_len=50, is_global=False):
        """
        Initializes the Z-Score detector with customizable parameters.

        :param window_len: Size of the window to calculate statistics (default=50).
        :param is_global: Whether to detect anomalies globally (default=False).
        """
        self.window_len = window_len
        self.detector = ZScoreDetector(is_global=is_global)

        # Sliding window to store recent data points
        self.data_window = []

    def detect(self, value):
        """
        Detects if the provided value is an anomaly using the Z-Score method.
        
        :param value: The new data point to analyze.
        :return: Anomaly score (higher values indicate higher anomaly likelihood).
        """
        # Add value to the sliding window
        self.data_window.append(value)

        # Limit the window to the specified size
        if len(self.data_window) > self.window_len:
            self.data_window.pop(0)

        # Calculate anomaly score using the ZScoreDetector from StreamAD
        score = self.detector.fit_score(np.array(self.data_window[-1]))
        return score
