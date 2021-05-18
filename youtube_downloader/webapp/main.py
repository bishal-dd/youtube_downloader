from pytube import YouTube


class Download(object):
    def __init__(self, link):
        self.link = link

    def youtube_video(self):
        yt = YouTube(str(self.link))
        video = yt.streams.first()
        video.download('C:/Users/user/Downloads/')

    def thumbnail(self):
        return YouTube(self.link).thumbnail_url
