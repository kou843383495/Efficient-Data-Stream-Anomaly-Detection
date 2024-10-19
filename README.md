# Efficient-Data-Stream-Anomaly-Detection

## The project is part of application of Graduate Software Engineer role at Cobblestone Energy

The goal of this project is to implement a simple and efficient anomaly detection algorithm that can find anomalous data points from continuous time series data.

The core code of this project includes the following aspects

- generate time series data
- anomaly detection algorithm
- visual page
---

In online-anomaly-detection/anomaly_detection/generate_data.py, use the equation:

y = year * w1 + season * w2 + month * w3 + weekday * w4 + day * w5 + t * w6

to construct a function related to the year, season, month, week, etc. of a time point. Assume that the function is the distribution function of a time series D, and there is a certain probability (p = 0.05) that an outlier will appear.In this project, data from 2019 to 2020 were simulated and random noise was added.

---

In this project, an adjusted z-score algorithm is used to find abnormal data.In the standard z algorithm, the difference between the actual distribution and the expected distribution should obey the random distribution, and the mean μ and standard deviation σ of the prediction error can be obtained. By comparing the error of a data point with the difference between the error mean (X - μ) and the standard deviation, it can be determined whether the point is abnormal data.

In this project, the mean μ and standard deviation σ of the prediction errors are no longer calculated for all prediction errors, but for the prediction errors over a period of time. This improvement enables the adjusted algorithm to adapt to some simple concept drift.

---

This project uses Django to implement a webpage to showcase the above work. The webpage allows users to select different weights to generate different distributions and view the results of abnormal predictions.
