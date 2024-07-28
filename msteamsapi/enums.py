# -*- coding: utf-8 -*-
from enum import Enum


class ContainerStyle(Enum):
    DEFAULT = "default"
    EMPHASIS = "emphasis"
    GOOD = "good"
    ATTENTION = "attention"
    WARNING = "warning"
    ACCENT = "accent"


class TextSize(Enum):
    DEFAULT = "default"
    SMALL = "small"
    MEDIUM = "medium"
    LARGE = "large"
    EXTRALARGE = "extraLarge"


class TextWeight(Enum):
    DEFAULT = "default"
    LIGHTER = "lighter"
    BOLDER = "bolder"


class BackgroundFillMode(Enum):
    COVER = "cover"
    REPEATHORIZONTALLY = "repeatHorizontally"
    REPEATVERTICALLY = "repeatVertically"
    REPEAT = "repeat"


class BackgroundHorizontalAlignment(Enum):
    LEFT = "left"
    CENTER = "center"
    RIGHT = "right"


class BackgroundVerticalAlignment(Enum):
    TOP = "top"
    CENTER = "center"
    BOTTOM = "bottom"
