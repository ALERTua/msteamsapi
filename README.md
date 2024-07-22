# Microsoft Teams AdaptiveCards API Wrapper for Python 2 and 3

Repository: https://github.com/ALERTua/msteamsapi

## Usage

- `pip install msteamsapi`
- Get a Workflow Webhook URL for your MSTeams non-private(!) channel using the standard template.
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

container = Container(style=ContainerStyle.DEFAULT)

card.mention('EMAIL', 'NAME', add_text_block=True)
mention_tag = card.mention('EMAIL', 'mention text')

container.add_text_block(
    'multiline\n\ntext\n\nmention 1: %s' % mention_tag,
    size=TextSize.DEFAULT, weight=TextWeight.DEFAULT, color="default")

factset = FactSet(('fact 1', 'fact 1 value'))
factset.add_facts(('fact 2', 'fact 2 value'), ('fact 3', 'fact 3 value'))
container.add_fact_set(factset)

card.add_container(container)

for i, url in enumerate(['https://google.com/', 'https://goo.gle']):
    card.add_url_button('url %s' % i, url)

webhook.add_cards(card)
webhook.send()
```
