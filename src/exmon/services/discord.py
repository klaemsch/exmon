import requests
from exmon.alarm import Alarm
from exmon.exceptions import ServiceExcpetion
from exmon.services import Service


class DiscordWebhook(Service):
    """ Discord Service sends exceptions to a discord webhook """
    _name: str = 'Discord Webhook'

    def __init__(self, url: str):
        """Create a new Discord Webhook Service.
        Given a URL to the Webhook it can send exception data to it.

        Args:
            url (:obj:`str`): URL to Discord Webhook.
        """
        self.url = str(url)

    def __call__(self, data: Alarm):
        """ send message string to discord webhook """

        data_str = (
            f'exmon reports an error with error code **{data.error_code}**.\n'
            f'```{data.get_formatted_traceback_string()}```'
        )

        data = {'content': data_str}
        try:
            resp = requests.post(url=self.url, json=data)
            resp.raise_for_status()
        except Exception as exc:
            raise ServiceExcpetion(self, exc) from exc
