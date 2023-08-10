import os
import numpy as np
import matplotlib.pyplot as plt

def time_domain_analysis(accel_data, file_name):
    # Extract time and accelerometer readings (X, Y, Z)
    time = accel_data[:, 0]
    accel_readings = accel_data[:, 1:]

    # Compute acceleration from X, Y, Z values (Euclidean norm)
    acceleration = np.linalg.norm(accel_readings, axis=1)

    # Time-domain analysis for acceleration
    mean_acceleration = np.mean(acceleration)
    median_acceleration = np.median(acceleration)
    std_acceleration = np.std(acceleration)

    # Numerical analysis for acceleration
    min_acceleration = np.min(acceleration)
    max_acceleration = np.max(acceleration)
    acceleration_range = max_acceleration - min_acceleration

    # Print the file name and time-domain analysis results for acceleration
    print(f"File: {file_name}")
    print("-----------------------------------------------------------------------")
    print("Time-Domain Analysis for Acceleration:")
    print(f"Mean Acceleration: {mean_acceleration}")
    print(f"Median Acceleration: {median_acceleration}")
    print(f"Acceleration Std Deviation: {std_acceleration}")
    print("-----------------------------------------------------------------------")

    # Print numerical analysis for acceleration
    print("Numerical Analysis for Acceleration:")
    print(f"Minimum Acceleration: {min_acceleration}")
    print(f"Maximum Acceleration: {max_acceleration}")
    print(f"Acceleration Range: {acceleration_range}")
    print("-----------------------------------------------------------------------")
    print("-----------------------------------------------------------------------")

    # Plot the accelerometer data for acceleration over time
    plt.plot(time, acceleration, label='Acceleration', linestyle='dashed', linewidth=2)
    plt.xlabel('Time')
    plt.ylabel('Acceleration')
    plt.title('Acceleration over Time')
    plt.legend()
    plt.show()

    return mean_acceleration, median_acceleration, std_acceleration

# Folder path containing accelerometer data files
# data/{ascending, decending, falling, resting and walking}
folder_path = 'data/falling'

# List all files in the folder
file_names = os.listdir(folder_path)

# Initialize lists to store results for each action
mean_acceleration_list = []
median_acceleration_list = []
std_acceleration_list = []

for file_name in file_names:
    # Construct the full file path
    file_path = os.path.join(folder_path, file_name)

    # Load accelerometer data from the text file using NumPy's genfromtxt function
    accel_data = np.genfromtxt(file_path, delimiter=',', skip_header=1)

    # Perform time-domain analysis for each file and print results with file name
    mean_acceleration, median_acceleration, std_acceleration = time_domain_analysis(accel_data, file_name)

    # Append results for each action to the respective lists
    mean_acceleration_list.append(mean_acceleration)
    median_acceleration_list.append(median_acceleration)
    std_acceleration_list.append(std_acceleration)

# Calculate summary statistics for acceleration across all files
overall_mean_acceleration = np.mean(mean_acceleration_list)
overall_median_acceleration = np.median(median_acceleration_list)
overall_std_acceleration = np.mean(std_acceleration_list)

# Print the summary statistics for acceleration across all files
print("Summary Statistics for Acceleration:")
print(f"Overall Mean Acceleration: {overall_mean_acceleration}")
print(f"Overall Median Acceleration: {overall_median_acceleration}")
print(f"Overall Acceleration Std Deviation: {overall_std_acceleration}")