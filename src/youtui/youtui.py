from textual.app import App, ComposeResult, on
from textual.widgets import Button, Header, Footer, Static

from youtui.widgets.yt_input import YT_Input

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
    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.dark = not self.dark
