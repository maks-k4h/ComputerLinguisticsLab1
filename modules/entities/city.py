
from .abstract import NamedEntityType


class City(NamedEntityType):
    @property
    def type_name(self) -> str:
        return 'City'
