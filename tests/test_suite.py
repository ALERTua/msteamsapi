# -*- coding: utf-8 -*-
import os
import sys

from dotenv import load_dotenv

from msteamsapi import ContainerStyle, FactSet, Container, AdaptiveCard, TeamsWebhook, TextSize, TextWeight

load_dotenv()

MSTEAMS_TEST_HOOK = os.getenv("MSTEAMS_TEST_HOOK")
MSTEAMS_TEST_EMAIL = os.getenv("MSTEAMS_TEST_EMAIL")
MSTEAMS_TEST_NAME = os.getenv("MSTEAMS_TEST_NAME")


def test_happy_pass():
    assert MSTEAMS_TEST_HOOK
    webhook = TeamsWebhook(MSTEAMS_TEST_HOOK)
    title = "Python %s" % sys.version.split(" ")[0]
    print(f"You should now receive an AdaptiveCard with title: {title}")
    card = AdaptiveCard(title=title, title_style=ContainerStyle.DEFAULT)
    container = Container(style=ContainerStyle.DEFAULT)

    card.mention(MSTEAMS_TEST_EMAIL, MSTEAMS_TEST_NAME, add_text_block=True)
    mention_tag = card.mention(MSTEAMS_TEST_EMAIL, "this dude")

    container.add_text_block(
        "multiline\n\ntext\n\nmention 1: %s" % mention_tag,
        size=TextSize.DEFAULT,
        weight=TextWeight.DEFAULT,
        color="default",
    )

    factset = FactSet(("fact 1", "fact 1 value"))
    factset.add_facts(("fact 2", "fact 2 value"), ("fact 3", "fact 3 value"))
    container.add_fact_set(factset)

    card.add_container(container)

    for i, url in enumerate(["https://google.com/", "https://goo.gle"]):
        card.add_url_button("url %s" % i, url)

    webhook.add_cards(card)
    webhook.send()
