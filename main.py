from textual.app import App, ComposeResult
from textual.containers import Container, Horizontal, Vertical
from textual.widgets import Header, Footer, Static, DataTable, Button, Label
from textual.binding import Binding

# Test data - will be replaced by real Matter client later
TEST_DEVICES = [
    {"node_id": "1", "name": "Living Room Light", "type": "Bulb", "status": "Online"},
    {"node_id": "2", "name": "Front Door Lock", "type": "Lock", "status": "Online"},
    {"node_id": "3", "name": "Thermostat", "type": "Climate", "status": "Offline"},
]


class MatterDeviceTable(Static):
    """Widget to display Matter devices."""

    def compose(self) -> ComposeResult:
        total = len(TEST_DEVICES)
        online = sum(1 for d in TEST_DEVICES if d["status"] == "Online")
        offline = total - online

        yield Label(
            f"Matter Devices ({total} total, {online} online, {offline} offline)",
            classes="section-title"
        )

        table = DataTable()
        table.add_columns("Node ID", "Name", "Type", "Status")

        for device in TEST_DEVICES:
            table.add_row(
                device["node_id"],
                device["name"],
                device["type"],
                device["status"]
            )

        yield table


class MatterTUI(App):
    """A Textual app to manage Matter/Thread devices."""

    TITLE = "Matter/Thread Network Manager"
    CSS = """
    Screen {
        background: $surface;
    }

    .section-title {
        background: $primary;
        color: $text;
        padding: 1;
        text-align: center;
        text-style: bold;
    }

    DataTable {
        height: 1fr;
        margin: 1 2;
    }

    #controls {
        height: auto;
        padding: 1 2;
        background: $panel;
    }

    Button {
        margin: 0 1;
    }
    """

    BINDINGS = [
        Binding("q", "quit", "Quit"),
        Binding("r", "refresh", "Refresh"),
    ]

    def compose(self) -> ComposeResult:
        yield Header()
        yield MatterDeviceTable()
        yield Container(
            Horizontal(
                Button("Refresh Devices", id="refresh", variant="primary"),
                Button("Commission Device", id="commission", variant="success"),
                Button("Settings", id="settings"),
                id="controls",
            )
        )
        yield Footer()

    def action_refresh(self) -> None:
        """Refresh the device list."""
        self.notify("Refreshing device list...")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button presses."""
        if event.button.id == "refresh":
            self.action_refresh()
        elif event.button.id == "commission":
            self.notify("Device commissioning not yet implemented")
        elif event.button.id == "settings":
            self.notify("Settings not yet implemented")


def main():
    app = MatterTUI()
    app.run()


if __name__ == "__main__":
    main()
