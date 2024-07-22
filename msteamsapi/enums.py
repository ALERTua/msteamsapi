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
