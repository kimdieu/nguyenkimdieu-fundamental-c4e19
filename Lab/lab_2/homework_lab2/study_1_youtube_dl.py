from youtube_dl import YoutubeDL

# sample 1,2: Download one video and more
# dl = YoutubeDL ()
# dl.download(['https://www.youtube.com/watch?v=w7PLmEFkgPI','https://www.youtube.com/watch?v=jOJbXvjZ-cQ'])


# Sample 3: Download audio
# options = {
#     'format': 'bestaudio/audio' # Tell the downloader to download only the best quality of audio
# }
# dl = YoutubeDL(options)
# dl.download(['https://www.youtube.com/watch?v=aJOTlE1K90k'])



# Sample 4: Search and then download the first video
options = {
    'default_search': 'ytsearch', # tell downloader to search instead of directly downloading
    'max_downloads': 1 # Tell downloader to download only the first entry (video)
}
dl = YoutubeDL(options)
dl.download(["Ánh nắng của anh"])
