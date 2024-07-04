import sys
import os
from pytube import YouTube
from moviepy.editor import VideoFileClip

def download_video(url):
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        video_title = yt.title.replace(" ", "_").replace("/", "_")  # Replace spaces and slashes with underscores
        video_filename = f"{video_title}.mp4"
        print(f"Downloading {yt.title}...")
        stream.download(filename=video_filename)
        print("Download completed!")
        return video_filename
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def extract_audio(video_path, output_folder="audio_tracks"):
    try:
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        
        video_clip = VideoFileClip(video_path)
        audio_path = os.path.join(output_folder, os.path.splitext(os.path.basename(video_path))[0] + ".mp3")
        video_clip.audio.write_audiofile(audio_path)
        video_clip.close()
        print(f"Audio extracted and saved to {audio_path}")
    except Exception as e:
        print(f"An error occurred during audio extraction: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python download_and_extract_audio.py <video_url>")
    else:
        video_url = sys.argv[1]
        video_path = download_video(video_url)
        if video_path:
            extract_audio(video_path)
