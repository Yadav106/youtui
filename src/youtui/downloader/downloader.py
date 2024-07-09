from typing import Dict
import yt_dlp
from textual.app import ComposeResult
from textual.widget import Widget
from textual.widgets import ProgressBar

# progress_hooks:    A list of functions that get called on download
#                    progress, with a dictionary with the entries
#                    * status: One of "downloading", "error", or "finished".
#                              Check this first and ignore unknown values.
#
#                    If status is one of "downloading", or "finished", the
#                    following properties may also be present:
#                    * filename: The final filename (always present)
#                    * tmpfilename: The filename we're currently writing to
#                    * downloaded_bytes: Bytes on disk
#                    * total_bytes: Size of the whole file, None if unknown
#                    * total_bytes_estimate: Guess of the eventual file size,
#                                            None if unavailable.
#                    * elapsed: The number of seconds since download started.
#                    * eta: The estimated time in seconds, None if unknown
#                    * speed: The download speed in bytes/second, None if
#                             unknown
#                    * fragment_index: The counter of the currently
#                                      downloaded video fragment.
#                    * fragment_count: The number of fragments (= individual
#                                      files that will be merged)
#
#                    Progress hooks are guaranteed to be called at least once
#                    (with status "finished") if the download is successful.

class ProgressBarWidget(ProgressBar):
    def __init__(self):
        super().__init__()
        self.styles.height = "auto"
        self.total = 100
        self.hidden = True

class DownloaderWidget(Widget):

    DEFAULT_CSS="""
    DownloaderWidget {
        padding: 2;
        background: $secondary;
    }
    """

    def compose(self) -> ComposeResult:
        self.styles.height = "auto"
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
