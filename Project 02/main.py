import fun


if __name__ == "__main__":
    youtube_urls = fun.load_video_urls('video_urls.txt')
    for url in youtube_urls:
        fun.download_youtube_audio_with_metadata(url)