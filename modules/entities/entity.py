from .abstract import NamedEntityType


class NamedEntity:
    def __init__(
            self,
            name,
            position: int,
            entity_type: NamedEntityType,
    ) -> None:
        self._name = name
        self._position = position
        self._entity_type = entity_type

    @property
    def name(self) -> str:
        return self._name

    @property
    def position(self) -> int:
        return self._position

    @property
    def entity_type(self) -> NamedEntityType:
        return self._entity_type
