# Real-Time Anomaly Detection System

This project implements a real-time anomaly detection system using Z-Score analysis. It simulates a stream of data points and identifies anomalies based on statistical thresholds. The detected anomalies are visualized in real-time, allowing for immediate observation of any significant deviations in the data.

## Features

- Simulates a stream of data points.
- Uses Z-Score method for anomaly detection.
- Visualizes data points and detected anomalies in real-time.
- Configurable parameters for data simulation, window size, and anomaly threshold.

## Parameters

You can customize the following parameters in the main.py file:

-  num_data_points: The number of data points to simulate (default is 1000).
-  window_size: The size of the window for Z-score calculation (default is 100).
-  threshold: The Z-score threshold for flagging anomalies (default is 3).

## Requirements

To run this project, you need to have Python installed along with the following packages:

- `matplotlib`: For data visualization
- `numpy`: For numerical computations
- `scipy`: For statistical functions

You can install the required packages using the following command:

```bash
pip install -r requirements.txt

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/kdjayyyy/Data-Anomaly-Detector
   cd Data-Anomaly-Detector```

2. **Set up the environment**:
   Install all the required dependencies using pip
   ```bash
   pip install -r requirements.txt```

3. **Run the project**:
   Run the python script from the src folder.
   ```bash
   python src/main.py```

