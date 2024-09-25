from zscore_detector import ZScoreAnomalyDetector
from stream_simulator import DataStreamSimulator

class AnomalyDetectionSystem:
    def __init__(self, total_points=1000, zscore_window=100, anomaly_threshold=3):
        """
        Sets up the anomaly detection system with a data stream simulator and a Z-Score anomaly detector.

        :param total_points: Total number of data points to simulate.
        :param zscore_window: Size of the window for Z-score calculations.
        :param anomaly_threshold: Z-score value above which a data point is flagged as an anomaly.
        """
        self.stream_simulator = DataStreamSimulator()  # Initialize the data stream simulator
        self.anomaly_detector = ZScoreAnomalyDetector(window_len=zscore_window)  # Initialize the Z-Score detector
        self.total_points = total_points
        self.anomaly_threshold = anomaly_threshold

    def execute(self):
        """
        Executes the detection pipeline: creates a data stream and utilizes the Z-Score method for anomaly detection.
        """
        data_stream = self.stream_simulator.generate_data()  # Create the data stream

        # Process each data point in the stream for anomaly detection
        for _ in range(self.total_points):
            point = next(data_stream)  # Get the next data point
            z_score, anomaly_flag = self.anomaly_detector.detect(point)  # Detect anomaly
            if z_score > self.anomaly_threshold:  # Check against the threshold
                print(f"Detected anomaly with score: {z_score}")

