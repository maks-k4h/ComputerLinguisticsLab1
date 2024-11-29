from .abstract import NamedEntityType


class Country(NamedEntityType):
    @property
    def type_name(self) -> str:
        return 'Country'
