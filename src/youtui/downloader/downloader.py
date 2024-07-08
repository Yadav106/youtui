from typing import Dict
import yt_dlp
from textual.app import ComposeResult
from textual.widget import Widget
from textual.widgets import ProgressBar

class ProgressBarWidget(ProgressBar):
    def __init__(self):
        super().__init__()
        self.total = 100
        self.hidden = True

class DownloaderWidget(Widget):

    def compose(self) -> ComposeResult:
        yield ProgressBarWidget()

    def on_progress(self, d):
        if d["status"] == 'downloading' and d['total_bytes']:
            print(d['filename'])
            print((d['downloaded_bytes']/d['total_bytes']) * 100)
            self.query_one(ProgressBarWidget).update(progress=(d['downloaded_bytes']/d['total_bytes'] * 100))
            print('---------------------------------------------')

    def generate_opts(self) -> Dict:
        yt_opts = {
            # 'format': 'bestaudio',
            'format': 'best',
            'restrictfilenames': True,
            'noplaylist': True,
            'nocheckcertificate': True,
            'ignoreerrors': True,
            # 'postprocessors': [{
            #         'key': 'FFmpegExtractAudio',
            #         'preferredcodec': 'opus'
            #     },
            # ],
            'outtmpl': '%(title)s-%(id)s.%(ext)s',
            'quiet': True,
            'no_warnings': True,
            "noprogress": True,
            'progress_hooks': [self.on_progress],
            # 'writesubtitles': True,
        }

        return yt_opts

    

    def generate_ydl(self):
        return yt_dlp.YoutubeDL(self.generate_opts())
