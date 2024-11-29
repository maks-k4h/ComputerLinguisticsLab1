from abc import ABC, abstractmethod

from .. import entities


class AbstractRecognizer(ABC):
    @abstractmethod
    def recognize_all(self, text: str) -> list[entities.entity.NamedEntity]:
        pass
