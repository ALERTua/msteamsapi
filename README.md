[![Stand With Ukraine](https://raw.githubusercontent.com/vshymanskyy/StandWithUkraine/main/banner-direct-single.svg)](https://stand-with-ukraine.pp.ua)
[![Made in Ukraine](https://img.shields.io/badge/made_in-Ukraine-ffd700.svg?labelColor=0057b7)](https://stand-with-ukraine.pp.ua)
[![Stand With Ukraine](https://raw.githubusercontent.com/vshymanskyy/StandWithUkraine/main/badges/StandWithUkraine.svg)](https://stand-with-ukraine.pp.ua)
[![Russian Warship Go Fuck Yourself](https://raw.githubusercontent.com/vshymanskyy/StandWithUkraine/main/badges/RussianWarship.svg)](https://stand-with-ukraine.pp.ua)

# Microsoft Teams AdaptiveCards API Wrapper for Python 2 and 3

##### Repository: https://github.com/ALERTua/msteamsapi
##### PyPi: https://pypi.org/project/msteamsapi/

[![Package and PyPi Upload](https://github.com/ALERTua/msteamsapi/actions/workflows/python-package.yml/badge.svg)](https://github.com/ALERTua/msteamsapi/actions/workflows/python-package.yml)
[![DEV Package and TestPyPi Upload](https://github.com/ALERTua/msteamsapi/actions/workflows/python-dev-package.yml/badge.svg)](https://github.com/ALERTua/msteamsapi/actions/workflows/python-dev-package.yml)
[![Commit Checks](https://github.com/ALERTua/msteamsapi/actions/workflows/commit.yml/badge.svg)](https://github.com/ALERTua/msteamsapi/actions/workflows/commit.yml)


## Usage

- `pip install msteamsapi`
- Get a Workflow Webhook URL for your MSTeams non-private(!) channel using the standard template `Post to a channel when a webhook request is received`.
- Use the Webhook URL to instantiate `TeamsWebhook` class.
- Fill the `TeamsWebhook` with `AdaptiveCard`.
- Fill the `AdaptiveCard` with `Container`.
- Fill the `Container` with `FactSet`, `TextBlock`, etc.
- `send()` the `TeamsWebhook` instance.

Example from [tests/test_suite.py](tests/test_suite.py):

```python
from msteamsapi import TeamsWebhook, AdaptiveCard, Container, FactSet, ContainerStyle, TextWeight, TextSize

webhook = TeamsWebhook('your_webhook_url')

card = AdaptiveCard(title='card title', title_style=ContainerStyle.DEFAULT)
card.add_background(url="https://github.com/ALERTua/msteamsapi/raw/main/tests/background.png")

container = Container(style=ContainerStyle.DEFAULT)

card.mention('EMAIL', 'NAME', add_text_block=True)
mention_tag = card.mention('EMAIL', 'mention text')

container.add_image("image url", "image alt text")
container.add_text_block(
    'multiline\n\ntext\n\nmention 1: %s' % mention_tag,
    size=TextSize.DEFAULT, weight=TextWeight.DEFAULT, color="default"
)

factset = FactSet(('fact 1', 'fact 1 value'))
factset.add_facts(('fact 2', 'fact 2 value'), ('fact 3', 'fact 3 value'))
container.add_fact_set(factset)

card.add_container(container)

for i, url in enumerate(['https://google.com/', 'https://goo.gle']):
    card.add_url_button('url %s' % i, url)

webhook.add_cards(card)
webhook.send()
```

Your [contribution](CONTRIBUTING.md) is appreciated.
