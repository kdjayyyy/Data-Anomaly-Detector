import matplotlib.pyplot as plt

class DataVisualizer:
    def __init__(self):
        """
        Initializes the visualizer for plotting data in real-time.

        - Sets up an interactive plot with a line for regular data and markers for anomalies.
        - Activates matplotlib's interactive mode for continuous updates.
        """
        plt.ion()  # Turn on interactive mode
        self.fig, self.ax = plt.subplots()  # Create figure and axes

        # Initialize plot elements
        self.data_line, = self.ax.plot([], [], label='Data Stream')
        self.anomaly_markers, = self.ax.plot([], [], 'ro', label='Anomalies')

        self.data_stream = []  # List for streaming data points
        self.anomaly_list = []  # Holds (index, value) for anomalies

        # Set plot labels and title
        self.ax.set_xlabel('Data Point Index')
        self.ax.set_ylabel('Value')
        self.ax.set_title('Real-Time Data Visualization')
        self.ax.legend()

    def update(self, value, is_anomaly):
        """
        Adds a new data point to the visualization and checks for anomalies.

        :param value: The new data point.
        :param is_anomaly: Indicates if the point is an anomaly.
        """
        self.data_stream.append(value)  # Update the data stream

        if is_anomaly:
            self.anomaly_list.append((len(self.data_stream) - 1, value))  # Log anomaly

        self._update_plot()  # Update the visual representation

    def _update_plot(self):
        """ Updates the plot with the latest data and anomalies. """
        self._set_data_line()
        self._set_anomaly_markers()
        self._adjust_plot_view()

    def _set_data_line(self):
        """ Sets the data line for the current data stream. """
        self.data_line.set_data(range(len(self.data_stream)), self.data_stream)

    def _set_anomaly_markers(self):
        """ Updates the plot to display anomalies as red circles. """
        if self.anomaly_list:
            anomaly_x, anomaly_y = zip(*self.anomaly_list)
        else:
            anomaly_x, anomaly_y = [], []
        self.anomaly_markers.set_data(anomaly_x, anomaly_y)

    def _adjust_plot_view(self):
        """
        Adjusts the axis limits dynamically based on the data and pauses briefly
        to allow for visual updates.
        """
        self.ax.relim()  # Recompute the data limits
        self.ax.autoscale_view()  # Automatically scale the view

        plt.pause(0.01)  # Pause for a brief moment to update the plot

    def show(self):
        """ Finalizes the plot for display after processing all data points. """
        plt.ioff()  # Turn off interactive mode
        plt.show()  # Show the plot
