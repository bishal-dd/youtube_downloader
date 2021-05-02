from pytube import YouTube


class Download(object):
    def __init__(self, download_link, file_location):
        self.download_link = download_link
        self.file_location = file_location

    def youtube_video(self):
        link = input(self.download_link)
        yt = YouTube(link)
        video = yt.streams.first()
        video.download(self.file_location)

