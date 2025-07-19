import os
import sys
import subprocess
import shutil
from concurrent.futures import ProcessPoolExecutor

def check_ffmpeg_installed():
    if shutil.which("ffmpeg") is None:
        print("""
[❌] FFmpeg not found on your system.

FFmpeg is required for this script to work.
Please install it from: https://ffmpeg.org/download.html

Windows:
    https://www.gyan.dev/ffmpeg/
    (add ffmpeg/bin to your PATH)

macOS:
    brew install ffmpeg

Linux:
    sudo apt install ffmpeg

Exiting.
""")
        sys.exit(1)

def find_matching_audio(audio_dir, base_name, extensions=None):
    if extensions is None:
        extensions = [".mka", ".mp3", ".aac", ".wav", ".flac", ".ogg"]

    for ext in extensions:
        candidate = os.path.join(audio_dir, base_name + ext)
        if os.path.isfile(candidate):
            return candidate
    return None

def is_video_supported_by_ffmpeg(filepath):
    try:
        result = subprocess.run(
            ["ffmpeg", "-v", "error", "-i", filepath, "-f", "null", "-"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        return result.returncode == 0
    except Exception:
        return False

def add_audio_track(args):
    filename, video_dir, audio_dir, output_dir = args

    full_path = os.path.join(video_dir, filename)
    if not os.path.isfile(full_path):
        return

    base_name, _ = os.path.splitext(filename)

    if not is_video_supported_by_ffmpeg(full_path):
        print(f"[❌] Unsupported video format: {filename}")
        return

    audio_path = find_matching_audio(audio_dir, base_name)
    if not audio_path:
        print(f"[❌] No matching audio found for: {filename}")
        return

    output_path = os.path.join(output_dir, base_name + "_with_dual_audio.mkv")

    cmd = [
        "ffmpeg",
        "-y",
        "-i", full_path,
        "-i", audio_path,
        "-map", "0",
        "-map", "1:a",
        "-c", "copy",
        "-shortest",
        output_path
    ]

    print(f"[🔄] Merging: {filename} + {os.path.basename(audio_path)}")

    try:
        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"[✅] Success: {output_path}")
    except Exception as e:
        print(f"[⚠️] Failed to process {filename}: {e}")

def main():
    print('|------------------------------------------------------------------------|')
    print('|--------------Batch applying audio files to video v.0.0.2---------------|')
    print('|---------Developed by Ilias Fasikhov 2025 (iliasfasikhov@gmail.com)-----|')
    print('|------------------------------------------------------------------------|')
    print()
    print('TIP: Matching is done by filename, e.g. "episode1.mkv" + "episode1.mka"\n')

    check_ffmpeg_installed()

    if len(sys.argv) != 4:
        print("Usage: python apply_audio.py <video_dir> <audio_dir> <output_dir>")
        sys.exit(1)

    video_dir, audio_dir, output_dir = sys.argv[1:4]
    os.makedirs(output_dir, exist_ok=True)

    all_files = os.listdir(video_dir)
    video_files = [f for f in all_files if os.path.isfile(os.path.join(video_dir, f))]

    if not video_files:
        print("[ℹ️] No video files found in the input directory.")
        sys.exit(0)

    with ProcessPoolExecutor() as executor:
        executor.map(add_audio_track, [
            (f, video_dir, audio_dir, output_dir) for f in video_files
        ])

if __name__ == "__main__":
    main()
