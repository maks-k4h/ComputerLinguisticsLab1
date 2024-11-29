from abc import abstractmethod, ABC


class NamedEntityType:
    @property
    @abstractmethod
    def type_name(self) -> str:
        pass
