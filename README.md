# Video Converter - Batch Audio Merger

A Python script that batch applies audio files to video files using FFmpeg. This tool automatically matches audio files with video files by filename and merges them into new video files with dual audio tracks.

## Features

- 🎬 Batch processing of video files
- 🎵 Automatic audio-video matching by filename
- 🔄 Parallel processing for better performance
- 📁 Organized output with descriptive filenames
- ✅ Support for multiple audio formats (MKA, MP3, AAC, WAV, FLAC, OGG)
- 🛡️ Built-in FFmpeg validation and error handling

## Prerequisites

- Python 3.6 or higher
- FFmpeg installed and accessible from PATH

### Installing FFmpeg

**Windows:**
- Download from [Gyan.dev](https://www.gyan.dev/ffmpeg/)
- Add ffmpeg/bin to your PATH environment variable

**macOS:**
```bash
brew install ffmpeg
```

**Linux:**
```bash
sudo apt install ffmpeg
```

## Usage

```bash
python apply-audio.py <video_dir> <audio_dir> <output_dir>
```

### Example

```bash
python apply-audio.py ./video ./audio ./merged
```

## File Matching

The script matches files by their base filename (without extension):

- `episode01.mkv` + `episode01.mka` → `episode01_with_dual_audio.mkv`
- `movie.mp4` + `movie.flac` → `movie_with_dual_audio.mkv`

## Project Structure

```
video_converter/
├── apply-audio.py          # Main script
├── video/                  # Input video files
├── audio/                  # Input audio files
├── merged/                 # Output files with merged audio
├── README.md              # This file
└── LICENSE                # License file
```

## Supported Formats

**Video:** Any format supported by FFmpeg (MP4, MKV, AVI, MOV, etc.)

**Audio:** MKA, MP3, AAC, WAV, FLAC, OGG

**Output:** MKV format with dual audio tracks

## How It Works

1. **Validation:** Checks if FFmpeg is installed
2. **File Discovery:** Scans video directory for supported files
3. **Matching:** Finds corresponding audio files by filename
4. **Processing:** Uses FFmpeg to merge video and audio streams
5. **Output:** Creates new files with both original and additional audio tracks

## Error Handling

- ❌ Missing FFmpeg installation
- ❌ Unsupported video formats
- ❌ Missing matching audio files
- ⚠️ Processing failures with detailed error messages

## Performance

The script uses parallel processing to handle multiple files simultaneously, significantly reducing processing time for large batches.

## Version

Current version: 0.0.2

## Author

Developed by Ilias Fasikhov (iliasfasikhov@gmail.com) - 2025

## License

This project is licensed under a Non-Commercial License - see the [LICENSE](LICENSE) file for details.

## Contributing

This project is for non-commercial use only. Please respect the license terms when using or modifying this software.
