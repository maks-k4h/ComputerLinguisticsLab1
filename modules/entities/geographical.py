from .abstract import NamedEntityType


class Geographical(NamedEntityType):
    @property
    def type_name(self) -> str:
        return 'Geographical'
