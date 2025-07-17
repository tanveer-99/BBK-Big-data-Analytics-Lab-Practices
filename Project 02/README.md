# Part 1: Audio Download Pipeline & Logging
## Step 1: Collect Video URLs
In this step, 10 random youtube video links have been saved to a file called `video_urls.txt`, ensuring each link in a separate line.
```python
https://www.youtube.com/watch?v=HhiBpR20RHE&list=RDHhiBpR20RHE&start_radio=1
https://www.youtube.com/watch?v=RCCz1WdU-D0&list=RDHhiBpR20RHE&index=3
https://www.youtube.com/watch?v=dJibiqUMxXk&list=RDdJibiqUMxXk&start_radio=1
https://www.youtube.com/watch?v=zjplA5XnacE&list=RDzjplA5XnacE&start_radio=1
https://www.youtube.com/watch?v=gJLVTKhTnog&list=RDMMgJLVTKhTnog&start_radio=1
https://www.youtube.com/watch?v=AGsn2ycFRqI&list=RDAGsn2ycFRqI&start_radio=1
https://www.youtube.com/watch?v=Ib_L3vuUX5k&list=RDMM&start_radio=1&rv=AGsn2ycFRqI
https://www.youtube.com/watch?v=JgDNFQ2RaLQ&list=RDJgDNFQ2RaLQ&start_radio=1
https://www.youtube.com/watch?v=BefnUx8wHxo
https://www.youtube.com/shorts/tnCvXqplP4w
```

## Step 2: Load the URLs into Python
The code below loads the text file into python and after stripping it, stores it in the `urls` array.
```python
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
```

## Step 3: Download audio and metadata
For this step, the boilercode that is provided is used with additional `log_download_status` function that logs the download info in a `download_log.txt` file stored in logs folder.
```python
LOGS_DIR = "logs"
os.makedirs(LOGS_DIR, exist_ok=True)

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
```
The `get_video_info` extracts the metadata from the youtube video and saves the audio file with `yt_dlp`.


The `extract_metadata` function extracts and returns a simplified dictionary with key metadata from a
video info object.


The `save_metadata_to_file` function saves the metadata info into a JSON file. 


The `download_youtube_audio_with_metadata` function combines the funtions and orchestrates the full process.

The process is then implemented with serial runner and parallel runner that can download up to 5 videos simultaneously.
### Serial mode
```python
import time
import fun
def serial_runner(urls):
    start = time.perf_counter()
    for url in urls:
        fun.download_youtube_audio_with_metadata(url)
    end = time.perf_counter()
    print(f"Serial mode: {end-start}")
```
Usage: `serial_runner.serial.runner(youtube_urls)`
<br/>
The time taken to download these 10 youtube videos in serial mode is: `54.3501081999857` seconds

### Parallel mode
```python
import time
import fun
import concurrent.futures

def parallel_runner(url):
    start = time.perf_counter()
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(fun.download_youtube_audio_with_metadata, url)
    end = time.perf_counter()
    print(f"Parallel mode: {end-start}")
```
Usage: `parallel_runner.parallel_runner(youtube_urls)`
<br/>
The time taken to download these 10 youtube videos in parallel mode is: `49.509902799967676` seconds
<br/>
> Therefore, we can see that parallel version is faster than serial version. 

> The complexity in serial mode is simpler, with code simplicity and scalability options, whereas in parallel mode, the complexity gets complex and sometimes concurrency needs to be handled. Also, the system load and resource usage is much less in serial than in parallel

> time complexity for serial runner is O(n*m), where n is the number of tasks and m is the time taken for each task. <br/>
The time for parallel runner is O(n/p), p being the number of processes/threads running in parallel. 

> The space complexity is less in serial than in parallel.

> However, the severe waiting due to I/O or, network speed limitation, the performance will depend on. In our case, the network speed might be low or because of the low configuration machine, there is not a significant change shown, although less than serial.

