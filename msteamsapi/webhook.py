# -*- coding: utf-8 -*-
import requests


class TeamsWebhook(object):
    def __init__(self, webhook_url):
        self.webhook_url = webhook_url
        self.payload = dict(attachments=[])

    def add_cards(self, *cards):
        """
        Adds adaptive cards to the payload.

        :param cards: One or more AdaptiveCard instances to add.
        :return: Response object from the webhook request.
        @type cards: *AdaptiveCard
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
        """
        headers = {"Content-Type": "application/json"}
        response = requests.post(self.webhook_url, headers=headers, json=self.payload)
        if response.status_code not in (200, 202):
            raise Exception("Failed to send card: %s, %s" % (response.status_code, response.text))

        return response
