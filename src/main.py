from zscore_anomaly_detection import ZScoreAnomalyDetector
from data_stream_simulator import DataStreamSimulator
from visualization import Visualizer

class AnomalyDetectionFramework:
    def __init__(self, total_points=1000, zscore_window=100, anomaly_threshold=3):
        """
        Initializes the framework for real-time anomaly detection.
        
        :param total_points: Total number of data points to simulate.
        :param zscore_window: Size of the window for Z-score calculations.
        :param anomaly_threshold: Z-score value above which a data point is flagged as an anomaly.
        """
        self.total_points = total_points  # Number of points to process
        self.stream_generator = DataStreamSimulator()  # Simulator for generating data
        self.detector = ZScoreAnomalyDetector(window_size=zscore_window, threshold=anomaly_threshold)  # Anomaly detection method
        self.visualization_tool = Visualizer()  # Tool for visualizing data

    def execute(self):
        """Runs the anomaly detection process for the specified amount of data points."""
        data_stream = self.stream_generator.generate_data()  # Start generating data stream

        for _ in range(self.total_points):  # Loop through the total number of data points
            current_value = next(data_stream)  # Get the next value from the data stream
            anomaly_flag = self.detector.is_anomaly(current_value)  # Check if the current value is an anomaly
            self.detector.update(current_value)  # Update the detector with the new value
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