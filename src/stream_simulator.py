import numpy as np

class StreamSimulator:
    def __init__(self, num_points=1000):
        """
        Initialize the stream simulator.
        
        :param num_points: Number of points to simulate in the data stream (default=1000).
        """
        self.num_points = num_points
    
    def generate_stream(self):
        """
        Generate a data stream with trend, seasonality, and random noise.
        
        :return: Simulated data stream as a numpy array.
        """
        # Create a linear trend
        trend = np.linspace(1, 100, self.num_points)
        
        # Add a seasonal component (sinusoidal pattern)
        seasonal = 10 * np.sin(np.linspace(0, 10 * np.pi, self.num_points))
        
        # Add random noise
        noise = np.random.normal(0, 5, self.num_points)
        
        # Combine all components
        return trend + seasonal + noise

