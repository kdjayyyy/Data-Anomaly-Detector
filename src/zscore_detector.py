import numpy as np

class ZScoreAnomalyDetector:
    def __init__(self, window_len=50, is_global=False):
        """
        Initializes the Z-Score detector with customizable parameters.

        :param window_len: Size of the window to calculate statistics (default=50).
        :param is_global: Whether to detect anomalies globally (default=False).
        """
        self.window_len = window_len
        self.is_global = is_global

        # Sliding window to store recent data points
        self.data_window = []

    def update(self, value):
        """
        Updates the sliding window with a new data point.
        
        :param value: The new data point to add to the window.
        """
        self.data_window.append(value)

        # Limit the window to the specified size
        if len(self.data_window) > self.window_len:
            self.data_window.pop(0)

    def detect(self, value):
        """
        Detects if the provided value is an anomaly using the Z-Score method.
        
        :param value: The new data point to analyze.
        :return: Tuple containing the Z-score and a boolean indicating if it's an anomaly.
        """
        self.update(value)

        if len(self.data_window) < self.window_len:
            return None, False  # Not enough data to compute Z-Score

        # Calculate mean and standard deviation
        mean = np.mean(self.data_window)
        std_dev = np.std(self.data_window)

        # Calculate the Z-Score
        z_score = (value - mean) / std_dev if std_dev > 0 else 0

        # Determine if the value is an anomaly
        is_anomaly = abs(z_score) > 3  # Using a threshold of 3 for anomaly detection

        return z_score, is_anomaly
