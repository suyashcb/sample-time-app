from datetime import datetime

from sample_time_app.app import ClockDisplay, build_display, render_screen


def test_build_display_formats_time_and_date() -> None:
    display = build_display(datetime(2026, 4, 14, 17, 8, 9))

    assert display == ClockDisplay(
        time_text="5:08:09 PM",
        date_text="Tuesday, April 14, 2026",
    )


def test_render_screen_includes_formatted_values() -> None:
    screen = render_screen(datetime(2026, 4, 14, 17, 8, 9))

    assert "Current Time and Date" in screen
    assert "Time: 5:08:09 PM" in screen
    assert "Date: Tuesday, April 14, 2026" in screen
