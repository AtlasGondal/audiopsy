# Audiopsy: Forensic Audio Analysis Tool

Audiopsy is a lightweight command-line tool designed to analyze audio files. It helps extract essential details like duration, channels, frame rate, and more. You can also generate waveform plots and save them for deeper investigation. Whether you’re working on audio research, forensic analysis, or just exploring sound files, Audiopsy is here to simplify the process.

---

## **What Audiopsy Can Do**

- Analyze audio files (`.mp3`, `.wav`) and extract technical details.
- Generate waveform plots for visual analysis.
- Save all results (CSV and waveform images) to a specified directory.
- Process single or multiple files with ease.

---

## **Getting Started**

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/AtlasGondal/audiopsy.git
   cd audiopsy
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Make sure `ffmpeg` is installed and available in your system's PATH:
   - **Linux**: `sudo apt install ffmpeg`
   - **MacOS**: `brew install ffmpeg`
   - **Windows**: Download from [ffmpeg.org](https://ffmpeg.org/) and add it to your PATH.

---

### Usage

```bash
# perform forensic analysis of audio files
python audiopsy.py -d /path/to/audio/files           # Analyze all audio files in a directory
python audiopsy.py -f file1.mp3,file2.wav            # Analyze specific files
python audiopsy.py -f file1.mp3 -o /path/to/output   # Specify where results should be saved
python audiopsy.py -f file1.mp3 -v                   # View waveforms during analysis
```

---

## **What You Get**

Audiopsy saves its results in the specified output directory (or a default `./output` directory):
1. **Audio Properties**: A CSV file (`audio_properties.csv`) listing details like duration, channels, and frame rate.
2. **Waveform Plots**: PNG images of each audio file's waveform for easy review.

---

## **Future Plans**

Here’s what I'm thinking for the next steps:
- **Noise Analysis**: Identify and quantify background noise.
- **Spectrogram Generation**: Add frequency-vs-time visualizations.
- **Clipping Detection**: Highlight distorted sections of audio.
- **Speech and Silence Detection**: Automatically detect speech and pauses.
- **Metadata Extraction**: Pull details like codec, creation date, and more.
- **Audio Comparisons**: Find similarities or differences between files.

If there’s something you’d love to see in Audiopsy, let me know!

---

## **Contributing**

Got ideas or improvements? Feel free to contribute:
1. Fork this repository.
2. Create a new branch: `git checkout -b feature-name`.
3. Commit your changes: `git commit -m "Add new feature"`.
4. Push your branch: `git push origin feature-name`.
5. Open a pull request.

---

## **License**

This project is licensed under the MIT License. Check the [LICENSE](LICENSE) file for more details.

---

## **Contact**

Have questions, suggestions, or just want to say hi? Open an issue here or reach out to me [here](https://atlasgondal.com/contact-me/?utm_source=self&utm_medium=github&utm_campaign=audiopsy&utm_term=git-description). 
