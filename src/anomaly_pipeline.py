from stream_simulator import StreamSimulator
from zscore_detector import ZScoreAnomalyDetector

class AnomalyDetectionSystem:
    def __init__(self):
        """
        Sets up the anomaly detection system with a stream simulator and a Z-Score anomaly detector.
        """
        self.stream_simulator = StreamSimulator()
        self.anomaly_detector = ZScoreAnomalyDetector()

    def execute(self):
        """
        Executes the detection pipeline: creates a data stream and utilizes the Z-Score method for anomaly detection.
        """
        data_stream = self.stream_simulator.generate_stream()  # Create the data stream

        # Process each data point in the stream for anomaly detection
        for point in data_stream:
            anomaly_score = self.anomaly_detector.detect(point)
            if anomaly_score > 3:  # Set threshold for anomalies (adjustable)
                print(f"Detected anomaly with score: {anomaly_score}")

