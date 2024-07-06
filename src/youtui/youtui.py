from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static

class YoutuiApp(App):
    BINDINGS = [
        ("q", "quit", "Quit")
    ]
    def compose(self) -> ComposeResult:
        self.title = "YouTUI"
        yield Header()
        yield Static("Youtui says Hello")
        yield Footer()
