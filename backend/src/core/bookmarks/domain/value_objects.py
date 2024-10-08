import dataclasses
from urllib.parse import urlparse, urlunparse
from src.core.shared.domain.value_object import ValueObject


@dataclasses.dataclass
class Title(ValueObject):
    value: str

    @staticmethod
    def create(value: str) -> 'Title':
        return Title(value=value)


@dataclasses.dataclass
class Link(ValueObject):
    value: str

    @staticmethod
    def is_valid_url(value: str) -> bool:
        parsed = urlparse(value)
        return all([parsed.scheme, parsed.netloc])

    @staticmethod
    def create(value: str) -> 'Link':
        if not Link.is_valid_url(value=value):
            raise ValueError()

        return Link(value=value)

