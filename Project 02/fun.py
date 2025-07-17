import yt_dlp
import certifi
import os
import json
from datetime import datetime



def load_video_urls(file_path):
    urls = []
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                urls.append(line.strip())
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
    return urls


OUTPUT_DIR = "audio_output"
LOGS_DIR = "logs"
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(LOGS_DIR, exist_ok=True)
os.environ["SSL_CERT_FILE"] = certifi.where()


def log_download_status(url: str, success: bool=True, error_msg: str = ''):
    timestamp = datetime.now().isoformat(timespec='seconds')
    log_entry = {
        "timestamp": timestamp,
        "url": url,
        "download": success,
        "error_msg": error_msg if not success else None
    }
    
    # save log info to the download_log.txt file
    log_file_path = os.path.join(LOGS_DIR, 'download_log.txt')
    with open(log_file_path, "a", encoding="utf-8") as log_file:
        json.dump(log_entry, log_file)
        log_file.write("\n")

def get_video_info(url: str, download: bool = True) -> dict:
    """Extract video info and optionally download the audio without warnings."""
    ydl_opts = {
        'format': 'bestaudio[ext=m4a]/bestaudio',
        'outtmpl': os.path.join(OUTPUT_DIR, '%(title)s.%(ext)s'),
        'noplaylist': True,
        'quiet': True,          # suppress general output
        'no_warnings': True,    # suppress warnings
        'skip_download': not download,
        'postprocessors': [],
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        return ydl.extract_info(url, download=download)
    
def extract_metadata(info: dict) -> dict:
    """Filter and return relevant metadata fields, including derived values."""
    upload_date = info.get("upload_date")
    tags = info.get("tags") or []

    return {
        "id": info.get("id"),
        "title": info.get("title"),
        "uploader": info.get("uploader"),
        "uploader_id": info.get("uploader_id"),
        "channel": info.get("channel"),
        "track": info.get("track"),
        "artist": info.get("artist"),
        "album": info.get("album"),
        "description": info.get("description"),
        "tags": tags,  # Ensure it's a list
        "duration_seconds": info.get("duration"),
        "upload_date": upload_date,
        "view_count": info.get("view_count"),
        "like_count": info.get("like_count"),
        "webpage_url": info.get("webpage_url"),

        # Derived fields
        "year_uploaded": int(upload_date[:4]) if upload_date else None,
        "tag_count": len(tags),
    }

def save_metadata_to_file(metadata: dict, title: str) -> str:
    """Save metadata as a JSON file and return the path."""
    safe_title = "".join(c for c in title if c.isalnum() or c in (" ", "_", "-")).rstrip()
    file_path = os.path.join(OUTPUT_DIR, f"{safe_title}.json")
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=2, ensure_ascii=False)
    return file_path

def download_youtube_audio_with_metadata(url: str):
    """Main function to download audio and save metadata."""
    print(f"\n🎵 Downloading: {url}")
    retries = 2
    attempt = 0
    while attempt<=retries:
        try:
            log_download_status(url)
            info = get_video_info(url)
            metadata = extract_metadata(info)
            json_path = save_metadata_to_file(metadata, metadata["title"])
            print(f"✅ Done: {metadata['title']}\n📄 Metadata: {json_path}")
        except Exception as e:
            attemp += 1
            print(f"❌ Failed to download: {url}\n   Error: {e}")
            log_download_status(url, success=False, error_msg=str(e))
            if attempt < retries:
                print(f"retrying for attemp number: {attempt+1}")
            if attempt == retries:
                print(f"Retry attempt failed for {url}.")
                break


        