import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def read_accelerometer_data(file_path):
    df = pd.read_csv(file_path, names=["Time", "X", "Y", "Z"], delimiter=",")
    return df

def frequency_domain_analysis(df):
    x_freq = np.fft.fft(df["X"])
    y_freq = np.fft.fft(df["Y"])
    z_freq = np.fft.fft(df["Z"])
    return x_freq, y_freq, z_freq

def power_spectrum_analysis(freq_data):
    power_spectrum = np.abs(freq_data)**2
    return power_spectrum

def plot_power_spectrum(ax, power_spectrum, axis_name, file_name):
    ax.plot(power_spectrum, label=axis_name)
    ax.set_xlabel("Frequency")
    ax.set_ylabel("Power")
    ax.set_title(f"Power Spectrum - {axis_name} ({file_name})")
    ax.legend()

def plot_acceleration(ax, df, axis_name):
    ax.plot(df["Time"], df["Acceleration"], label=f"{axis_name} Acceleration")
    ax.set_xlabel("Time (seconds)")
    ax.set_ylabel("Acceleration (m/s²)")
    ax.set_title(f"Acceleration vs. Time - {axis_name}")
    ax.legend()


def calculate_acceleration(df):
    # Calculate the magnitude of acceleration (3D vector) using Pythagorean theorem
    df["Acceleration"] = np.sqrt(df["X"]**2 + df["Y"]**2 + df["Z"]**2)
    return df

def plot_all_axes_power_spectra_with_acceleration(file_path):
    fig, axes = plt.subplots(2, 1, figsize=(10, 8), sharex=False)

    df = read_accelerometer_data(file_path)
    x_freq, y_freq, z_freq = frequency_domain_analysis(df)
    x_power_spectrum = power_spectrum_analysis(x_freq)
    y_power_spectrum = power_spectrum_analysis(y_freq)
    z_power_spectrum = power_spectrum_analysis(z_freq)

    plot_power_spectrum(axes[0], x_power_spectrum, "X-axis", os.path.basename(file_path))
    plot_power_spectrum(axes[0], y_power_spectrum, "Y-axis", os.path.basename(file_path))
    plot_power_spectrum(axes[0], z_power_spectrum, "Z-axis", os.path.basename(file_path))

    df = calculate_acceleration(df)

    plot_power_spectrum(axes[0], df["Acceleration"], "Acceleration", os.path.basename(file_path))

    plot_acceleration(axes[1], df, "Combined")

    plt.tight_layout()
    plt.show()

def perform_analysis_on_directory(directory_path):
    file_list = os.listdir(directory_path)
    for file_name in file_list:
        if file_name.endswith(".txt"):  # Assuming all accelerometer files have a .txt extension
            file_path = os.path.join(directory_path, file_name)
            plot_all_axes_power_spectra_with_acceleration(file_path)

if __name__ == "__main__":
    directory_path = "data/falling"
    perform_analysis_on_directory(directory_path)
