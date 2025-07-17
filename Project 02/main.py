import fun
import serial_runner
import parallel_runner


if __name__ == "__main__":
    youtube_urls = fun.load_video_urls('video_urls.txt')
    
    # serial_runner.serial_runner(youtube_urls)
    parallel_runner.parallel_runner(youtube_urls)