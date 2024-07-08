from textual import work
from textual.app import App, ComposeResult, on
from textual.widgets import Button, Header, Footer
from yt_dlp.downloader.websocket import asyncio

from youtui.widgets.yt_input import YT_Input
from youtui.downloader.downloader import DownloaderWidget


class YoutuiApp(App):
    BINDINGS = [
        ("q", "quit", "Quit"),
    ]

    def compose(self) -> ComposeResult:
        self.title = "YouTUI"
        yield Header()
        yield YT_Input(placeholder="Video URL")
        yield Button("Download")
        yield Footer()

    @on(Button.Pressed)
    @work()
    async def on_button_pressed(self) -> None:
        asyncio.create_task(self.download_video())

    async def download_video(self) -> None:
        newDownloader = DownloaderWidget()
        self.mount(newDownloader)
        await asyncio.to_thread(newDownloader.generate_ydl().download,self.query_one(YT_Input).value)
        self.exit()
