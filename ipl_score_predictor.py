import numpy as np

# 1 Dataset

# Runs scored by a team in last 20 matches
runs = np.array([
    178, 145, 201, 167, 190,
    210, 155, 189, 175, 162,
    205, 198, 134, 172, 183,
    160, 187, 199, 181, 154
])

# 2️ Basic Statistics

average_score = np.mean(runs)
highest_score = np.max(runs)
lowest_score = np.min(runs)
std_dev = np.std(runs)


# 3️ Outlier Detection

mean = average_score
std = std_dev

high_outliers = runs[runs > mean + 1.5 * std]
low_outliers = runs[runs < mean - 1.5 * std]


# 4️ Score Prediction


# Simple average prediction
simple_prediction = average_score

# Weighted prediction 
weights = np.linspace(1, 2, len(runs))  
weighted_prediction = np.average(runs, weights=weights)

# Monte Carlo Prediction 
samples = np.random.normal(mean, std, 1000)
monte_carlo_prediction = samples.mean()



print(" IPL Score Predictor")
print("-----------------------")

print("Basic Statistics")
print("Average Score:", average_score)
print("Highest Score:", highest_score)
print("Lowest Score:", lowest_score)
print("Standard Deviation:", std_dev)

print("-----------------------")


print("Outliers:")
print("High Outliers:", high_outliers)
print("Low Outliers:", low_outliers)


print("-----------------------")

print("Score Predictions:")
print("Simple Average Prediction:", simple_prediction)
print("Weighted Prediction:", weighted_prediction)
print("Monte Carlo Prediction:", monte_carlo_prediction)

print("-----------------------")

