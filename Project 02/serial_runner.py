import time
import fun
def serial_runner(urls):
    start = time.perf_counter()
    for url in urls:
        fun.download_youtube_audio_with_metadata(url)
    end = time.perf_counter()
    print(f"Serial mode: {end-start}")
    