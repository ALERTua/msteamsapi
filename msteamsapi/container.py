"""Container class module."""

from msteamsapi.enums import ContainerStyle, TextSize, TextWeight


class Container(object):  # https://adaptivecards.io/explorer
    """Container class."""

    def __init__(self, style=ContainerStyle.DEFAULT):
        """
        Container class constructor.

        :param style: Style of the container.
        :type style: ContainerStyle
        """
        self.container = {
            "type": "Container",
            "items": [],
            "style": style.value,
        }

    def _add_item(self, item):
        """
        Add an item to the container.

        :param item: The item to be added to the container.
        """
        self.container["items"].append(item)

    def add_fact_set(self, fact_set):
        """
        Add a fact set to the container.

        :param fact_set: An instance of the FactSet class.
        :type fact_set: FactSet
        """
        self._add_item(fact_set.payload)

    def add_text_block(self, text, size=TextSize.DEFAULT, weight=TextWeight.DEFAULT, color="default", wrap=None):
        """
        Add a text block to the container.

        The new line character should be used twice to add a new line.
        https://learn.microsoft.com/en-us/microsoftteams/platform/task-modules-and-cards/cards/cards-format?tabs=adaptive-md%2Cdesktop%2Cconnector-html

        :param text: The text content of the text block.
        :param size: The size of the text block (default: "default").
        :param weight: The weight of the text block (default: "default").
        :param color: The color of the text block (default: "default").
        """
        if wrap is None:
            wrap = False

        text_block = dict(type="TextBlock", text=text, size=size.value, weight=weight.value, color=color, wrap=wrap)
        self._add_item(text_block)

    def add_image(self, url, alt_text="Image"):
        """
        Add an image to the container.

        :param url: The URL of the image.
        :param alt_text: The alternate text for the image (default: "Image").
        """
        image = dict(type="Image", url=url, altText=alt_text)
        self._add_item(image)

    def to_dict(self):
        """
        Convert the container to a dictionary representation.

        :return: Dictionary representation of the container.
        """
        return self.container


class FactSet(object):
    """Class for adding facts to the payload."""

    def __init__(self, *facts):
        """
        Initialize a new instance of the FactSet class with the given facts.

        :param facts: A variable-length argument list of facts to add to the payload.
        :type facts: tuple
        """
        self.payload = {"type": "FactSet", "facts": []}
        if facts:
            self.add_facts(*facts)

    def add_fact(self, fact_title, fact_value):
        """
        Add a new fact to the payload.

        :param fact_title: Fact Title
        :type fact_title: str
        :param fact_value: Fact Value
        :type fact_value: str
        """
        self.payload["facts"].append({"title": fact_title, "value": fact_value})

    def add_facts(self, *facts):
        """
        Add facts to the payload as tuple of title and value.

        @type facts: tuple
        """
        for title, value in facts:
            self.add_fact(fact_title=title, fact_value=value)
