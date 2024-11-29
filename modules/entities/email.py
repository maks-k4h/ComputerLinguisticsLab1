from .abstract import NamedEntityType


class Email(NamedEntityType):
    @property
    def type_name(self) -> str:
        return 'Email'
