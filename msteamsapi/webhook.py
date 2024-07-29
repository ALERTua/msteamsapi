"""
Provides a class for sending messages to Microsoft Teams via a webhook.

The TeamsWebhook class allows you to create a webhook payload and send it to a Microsoft Teams channel.

Example usage:

```python
from msteamsapi.webhook import TeamsWebhook

# Create a new webhook instance
webhook = TeamsWebhook("https://example.com/webhook")

# Add an adaptive card to the payload
card = AdaptiveCard()
webhook.add_cards(card)

# Send the payload to the webhook
response = webhook.send()
```
"""

import requests


class TeamsWebhook(object):
    """TeamsWebhook class."""

    def __init__(self, webhook_url):
        """
        TeamsWebhook class constructor.

        :param webhook_url: The webhook URL.
        :type webhook_url: str
        """
        self.webhook_url = webhook_url
        self.payload = {"attachments": []}

    def add_cards(self, *cards):
        """
        Add adaptive cards to the payload.

        :param cards: One or more AdaptiveCard instances to add.
        :type cards: *AdaptiveCard
        :return: Response object from the webhook request.
        """
        cards = [
            {
                "contentType": "application/vnd.microsoft.card.adaptive",
                "contentUrl": None,
                "content": card.to_dict(),
            }
            for card in cards
        ]
        self.payload["attachments"].extend(cards)

    def send(self):
        """
        Send the payload via Microsoft Teams webhook.

        :return: Response object from the webhook request.
        :rtype: requests.Response
        :raises: Exception
        """
        headers = {"Content-Type": "application/json"}
        response = requests.post(self.webhook_url, headers=headers, json=self.payload, timeout=30)
        if response.status_code not in (200, 202):
            raise Exception("Failed to send card: %s, %s" % (response.status_code, response.text))

        return response
