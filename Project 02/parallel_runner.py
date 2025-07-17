import time
import fun
import concurrent.futures

def parallel_runner(url):
    start = time.perf_counter()
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(fun.download_youtube_audio_with_metadata, url)
    end = time.perf_counter()
    print(f"Parallel mode: {end-start}")