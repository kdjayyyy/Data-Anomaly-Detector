import numpy as np

class DataStreamSimulator:
    def __init__(self, num_points=1000):
        """
        Initialize the stream simulator.
        
        :param num_points: Number of points to simulate in the data stream (default=1000).
        """
        self.num_points = num_points
    
    def generate_data(self):
        """
        Generate a data stream with trend, seasonality, and random noise.
        
        :return: A generator that yields simulated data points.
        """
        # Create a linear trend
        trend = np.linspace(1, 100, self.num_points)
        
        # Add a seasonal component (sinusoidal pattern)
        seasonal = 10 * np.sin(np.linspace(0, 10 * np.pi, self.num_points))
        
        # Add random noise
        noise = np.random.normal(0, 5, self.num_points)
        
        # Combine all components
        data_stream = trend + seasonal + noise
        
        for value in data_stream:
            yield value  # Yield each data point

