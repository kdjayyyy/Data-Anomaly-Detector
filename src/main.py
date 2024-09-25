import numpy as np
import random
import matplotlib.pyplot as plt

from zscore_detector import ZScoreAnomalyDetector

class DataStreamSimulator:
    def __init__(self, mean=0, std_dev=1):
        """
        Initializes the data stream simulator.

        :param mean: Mean of the normal distribution.
        :param std_dev: Standard deviation of the normal distribution.
        """
        self.mean = mean
        self.std_dev = std_dev

    def generate_data(self):
        """Generates a stream of random data points."""
        while True:
            yield np.random.normal(self.mean, self.std_dev)

class Visualizer:
    def __init__(self):
        self.data_points = []
        self.anomalies = []

    def update(self, value, is_anomaly):
        """Updates the visualizer with the current value and its anomaly status."""
        self.data_points.append(value)
        if is_anomaly:
            self.anomalies.append(value)
        else:
            self.anomalies.append(None)

    def show(self):
        """Displays the visual representation of the data."""
        plt.figure(figsize=(12, 6))
        plt.plot(self.data_points, label='Data Points')
        plt.scatter(range(len(self.data_points)), self.anomalies, color='red', label='Anomalies', zorder=5)
        plt.title('Anomaly Detection')
        plt.xlabel('Data Point Index')
        plt.ylabel('Value')
        plt.legend()
        plt.show()

class AnomalyDetectionFramework:
    def __init__(self, total_points=1000, zscore_window=100, anomaly_threshold=3):
        """
        Initializes the framework for real-time anomaly detection.
        
        :param total_points: Total number of data points to simulate.
        :param zscore_window: Size of the window for Z-score calculations.
        :param anomaly_threshold: Z-score value above which a data point is flagged as an anomaly.
        """
        self.total_points = total_points
        self.stream_generator = DataStreamSimulator()  # Simulator for generating data
        self.detector = ZScoreAnomalyDetector(window_len=zscore_window)  # Anomaly detection method
        self.visualization_tool = Visualizer()  # Tool for visualizing data

    def execute(self):
        """Runs the anomaly detection process for the specified amount of data points."""
        data_stream = self.stream_generator.generate_data()  # Start generating data stream

        for _ in range(self.total_points):
            current_value = next(data_stream)  # Get the next value from the data stream
            z_score, anomaly_flag = self.detector.detect(current_value)  # Check if the current value is an anomaly
            self.visualization_tool.update(current_value, anomaly_flag)  # Visualize the current value and anomaly status

        self.visualization_tool.show()  # Finalize and display the visualization

def main():
    # Create and run an instance of the anomaly detection framework
    detection_system = AnomalyDetectionFramework(
        total_points=1000, 
        zscore_window=100, 
        anomaly_threshold=3
    )
    detection_system.execute()  # Start the anomaly detection process

if __name__ == "__main__":
    main()
