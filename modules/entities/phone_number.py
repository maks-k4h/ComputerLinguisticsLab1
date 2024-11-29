from . import abstract


class PhoneNumber(abstract.NamedEntityType):
    @property
    def type_name(self) -> str:
        return 'Phone Number'
