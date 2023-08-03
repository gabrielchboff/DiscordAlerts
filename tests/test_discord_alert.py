import pytest
from src.alerts.alerts import DiscordAlert


@pytest.fixture
def discord_alert():
    return DiscordAlert()


def test_send_alert(discord_alert):
    assert discord_alert.send_alert(
        "title", "message", 0x00ff00, "thumbnail")
