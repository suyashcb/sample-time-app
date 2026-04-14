from __future__ import annotations

import time
from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class ClockDisplay:
    time_text: str
    date_text: str


def build_display(now: datetime) -> ClockDisplay:
    return ClockDisplay(
        time_text=now.strftime("%I:%M:%S %p").lstrip("0"),
        date_text=now.strftime("%A, %B %d, %Y"),
    )


def render_screen(now: datetime) -> str:
    display = build_display(now)
    return (
        "\x1b[2J\x1b[H"
        "Current Time and Date\n"
        "=====================\n\n"
        f"Time: {display.time_text}\n"
        f"Date: {display.date_text}\n\n"
        "Press Ctrl+C to exit.\n"
    )


def main() -> None:
    try:
        while True:
            print(render_screen(datetime.now()), end="", flush=True)
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nGoodbye.")


if __name__ == "__main__":
    main()
