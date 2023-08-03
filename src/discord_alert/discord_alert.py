
from dataclasses import dataclass
from discord_webhook.webhook import DiscordWebhook


@dataclass(order=True)
class DiscordAlert:
    hook: str = ""

    def send_alert(self, title: str, message: str,
                   color: int, thumbnail_url: str
                   ) -> bool:
        embeds = [
            {
                "title": title,
                "description": message,
                "color": color,
                "thumbnail": {
                    "url": thumbnail_url
                },
            },
        ]
        try:
            webhook = DiscordWebhook(url=self.hook, embeds=embeds)
            webhook.execute()
            return True
        except Exception:
            return False
