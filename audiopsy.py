# Audiopsy: Forensic Audio Analysis Tool
# Author: Atlas Gondal

import os
import sys
import argparse
from pydub import AudioSegment
from tabulate import tabulate
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Banner Display
def display_banner():
    banner = r"""
     █████╗ ██╗   ██╗██████╗ ██╗ ██████╗ ██████╗ ██╗   ██╗
    ██╔══██╗██║   ██║██╔══██╗██║██╔═══██╗██╔══██╗╚██╗ ██╔╝
    ███████║██║   ██║██║  ██║██║██║   ██║██████╔╝ ╚████╔╝
    ██╔══██║██║   ██║██║  ██║██║██║   ██║██╔═══╝   ╚██╔╝
    ██║  ██║╚██████╔╝██████╔╝██║╚██████╔╝██║        ██║
    ╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚═╝ ╚═════╝ ╚═╝        ╚═╝

                 Forensic Audio Analysis
                   Author: Atlas Gondal
    """
    print(banner)

# Argument parser setup
def parse_arguments():
    parser = argparse.ArgumentParser(description="Audiopsy: Forensic Audio Analysis Tool")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "-d", "--directory", type=str, help="Path to the directory containing audio files"
    )
    group.add_argument(
        "-f", "--files", type=str, help="Comma-separated list of audio file paths to process"
    )
    parser.add_argument(
        "-o", "--output", type=str, default="output", help="Output directory to save results (default: ./output)"
    )
    parser.add_argument(
        "-v", "--view-waveforms", action="store_true", help="Flag to display waveforms during analysis"
    )
    return parser.parse_args()

# Function to fetch files
def fetch_files(args):
    if args.directory:
        # Fetch all audio files from the specified directory
        directory = args.directory
        if not os.path.isdir(directory):
            print(f"Error: {directory} is not a valid directory.")
            sys.exit(1)
        return [
            os.path.join(directory, f) for f in os.listdir(directory) if f.endswith(('.mp3', '.wav'))
        ]
    elif args.files:
        # Use the specified files
        files = [file.strip() for file in args.files.split(",")]
        for file in files:
            if not os.path.isfile(file):
                print(f"Error: {file} is not a valid file.")
                sys.exit(1)
        return files

# Function to analyze audio properties
def analyze_audio_properties(files, output_dir):
    properties = {
        "File": [],
        "Duration (seconds)": [],
        "Channels": [],
        "Frame Rate (Hz)": [],
        "Sample Width (bytes)": []
    }
    for file in files:
        audio = AudioSegment.from_file(file)
        properties["File"].append(file)
        properties["Duration (seconds)"].append(len(audio) / 1000)
        properties["Channels"].append(audio.channels)
        properties["Frame Rate (Hz)"].append(audio.frame_rate)
        properties["Sample Width (bytes)"].append(audio.sample_width)

    # Save results to a CSV file in the output directory
    df = pd.DataFrame(properties)
    csv_path = os.path.join(output_dir, "audio_properties.csv")
    df.to_csv(csv_path, index=False)
    print(f"Audio properties saved to: {csv_path}")
    return df

# Function to plot and save waveforms
def save_waveforms(files, output_dir, view_waveforms=False):
    for file in files:
        audio = AudioSegment.from_file(file)
        samples = np.array(audio.get_array_of_samples())
        # Adjust for stereo (two channels)
        if audio.channels == 2:
            samples = samples.reshape(-1, 2)
            samples = samples.mean(axis=1)  # Convert to mono for simplicity

        plt.figure(figsize=(12, 4))
        plt.plot(samples, color='gray')
        plt.title(f"Waveform of {os.path.basename(file)}")
        plt.xlabel("Sample")
        plt.ylabel("Amplitude")

        # Save the plot
        plot_path = os.path.join(output_dir, f"{os.path.basename(file)}_waveform.png")
        plt.savefig(plot_path)
        print(f"Waveform saved to: {plot_path}")

        # Display waveform if the flag is set
        if view_waveforms:
            plt.show()
        plt.close()

# Main Function
def main():
    display_banner()
    args = parse_arguments()

    # Create or verify output directory
    output_dir = args.output
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Created output directory: {output_dir}")
    else:
        print(f"Using existing output directory: {output_dir}")

    # Fetch audio files
    audio_files = fetch_files(args)
    if not audio_files:
        print("No audio files found. Exiting.")
        sys.exit(1)

    # Analyze and save audio properties
    print("\nAnalyzing Audio Properties...")
    audio_properties_df = analyze_audio_properties(audio_files, output_dir)
    print("\nAudio File Properties:")
    print(tabulate(audio_properties_df, headers='keys', tablefmt='pretty'))

    # Plot and save waveforms
    print("\nGenerating and Saving Waveform Plots...")
    save_waveforms(audio_files, output_dir, view_waveforms=args.view_waveforms)
    print("\nAnalysis Complete!")

if __name__ == "__main__":
    main()
