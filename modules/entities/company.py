from .abstract import NamedEntityType


class Company(NamedEntityType):
    @property
    def type_name(self) -> str:
        return 'Company'
