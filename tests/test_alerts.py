from dataclasses import dataclass
import pytest

from discord_alert.discord_alert import DiscordAlert

# TODO: Think about the decorator viability


@dataclass
class Alert:
    @staticmethod
    def alert(custom_msg=None):
        """
        Decorator function for error handling and sending alerts via webhook.

        Args:
            func (callable): The function to be wrapped.

        Returns:
            callable: The wrapped function.
        """

        def handler(func):
            def wrapper(*args, **kwargs):
                """
                Wrapper function that executes the wrapped function and handles any exceptions.

                Args:
                    *args: Positional arguments to be passed to the wrapped function.
                    **kwargs: Keyword arguments to be passed to the wrapped function.

                Returns:
                    None
                """
                try:
                    func(*args, **kwargs)  # Execute the wrapped function
                except Exception as e:
                    # Handle the exception by sending an alert via webhook

                    discord_alert = DiscordAlert()
                    discord_alert.send_alert(
                        'Alert sended via webhook', custom_msg+e, 0x00ff00, "thumbnail")
                    )
            return wrapper

        return handler


@ pytest.fixture
def alert():
    pass
