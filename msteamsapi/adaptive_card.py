# -*- coding: utf-8 -*-
import json

from msteamsapi.container import Container
from msteamsapi.enums import (ContainerStyle, TextSize, BackgroundVerticalAlignment,
                              BackgroundHorizontalAlignment, BackgroundFillMode)


class AdaptiveCard(object):
    """https://adaptivecards.io/explorer"""

    def __init__(self, title=None, title_style=ContainerStyle.DEFAULT, width="Full"):
        """

        @type title: str or unicode
        @type title_style: ContainerStyle
        """
        self.card = {
            "type": "AdaptiveCard",
            "version": "1.4",
            "body": [],
            "actions": [],
            "msteams": {
                "entities": [],
                "width": width,
                "allowExpand": True,
            },
        }
        if title and title_style:
            title_container = Container(style=title_style)
            title_container.add_text_block(text=title, size=TextSize.MEDIUM)
            self.add_container(title_container)

    def add_container(self, container):
        """
        Add a container to the adaptive card.

        :param container: The container object to add.
        :type container: Container
        """
        self.card["body"].append(container.to_dict())

    def add_background(self, url, fill_mode=None, horizontal_alignment=None, vertical_alignment=None):
        """
        https://adaptivecards.io/explorer/BackgroundImage.html

        :param url: The URL of the image.
        :type url: str
        :param fill_mode: The fill mode of the image.
        :type fill_mode: BackgroundFillMode
        :param horizontal_alignment: The horizontal alignment of the image.
        :type horizontal_alignment: BackgroundHorizontalAlignment
        :param vertical_alignment: The vertical alignment of the image.
        :type vertical_alignment: BackgroundVerticalAlignment
        """
        kw = dict(url=url)
        if fill_mode:
            kw["fillMode"] = fill_mode
        if horizontal_alignment:
            kw["horizontalAlignment"] = horizontal_alignment
        if vertical_alignment:
            kw["verticalAlignment"] = vertical_alignment
        self.card["backgroundImage"] = kw

    def add_action(self, action_type, title, url):
        """
        Add an action to the adaptive card.

        :param action_type: The type of action (e.g., "Action.OpenUrl").
        :param title: The title of the action.
        :param url: The URL the action points to.
        """
        action = dict(type=action_type, title=title, url=url)
        self.card["actions"].append(action)

    def add_url_button(self, title, url):
        """
        Add a button to the adaptive card.

        :param title: The title of the button.
        :type title: str or unicode
        :param url: The URL the button points to.
        :type url: str or unicode
        """
        action = dict(title=title, url=url, type="Action.OpenUrl")
        self.card["actions"].append(action)

    def mention(self, user_id, mention_text=None, add_text_block=False):
        """
        Add a mention to the adaptive card.
        https://learn.microsoft.com/en-us/microsoftteams/platform/task-modules-and-cards/cards/cards-format?tabs=adaptive-md%2Cdesktop%2Cconnector-html
        https://poszytek.eu/en/microsoft-en/office-365-en/powerautomate-en/how-to-mention-tags-users-channels-and-teams-using-power-automate/
        https://powerusers.microsoft.com/t5/Building-Flows/Ms-Teams-Mentions-in-adaptive-cards/m-p/522622#M66891

        :type user_id: str
        :param user_id: The user ID or email of the mentioned user.
        :type mention_text: str
        :param mention_text: The text in the card to mention the user.
        :type add_text_block: bool
        :param add_text_block: Adds a text block with the mention to the card.
        :rtype: str
        :return: The mention tag for the user.
        """
        mention_text = mention_text or user_id
        mention_tag = "<at>%s</at>" % mention_text
        mention = {
            "type": "mention",
            "text": mention_tag,
            "mentioned": {
                "id": user_id,
                "name": mention_text,
            },
        }
        self.card["msteams"]["entities"].append(mention)
        if add_text_block:
            mention_text_block = {
                "type": "TextBlock",
                "text": mention_tag,
            }
            self.card["body"].append(mention_text_block)
        return mention_tag

    def to_dict(self):
        """
        Convert the adaptive card to a dictionary representation.

        :return: Dictionary representation of the adaptive card.
        """
        return self.card

    def to_json(self):
        """
        Convert the adaptive card to a JSON string representation.

        :return: JSON string representation of the adaptive card.
        """
        return json.dumps(self.card, indent=4)
