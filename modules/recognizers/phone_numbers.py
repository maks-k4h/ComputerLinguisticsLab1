import re
from .abstract import AbstractRecognizer
from .. import entities
from . import data


class PhoneNumberRecognizer(AbstractRecognizer):
    def __init__(self) -> None:
        # Load the list of phone number patterns for different countries
        self._phone_number_patterns = data.phone_numbers.ALL_PHONE_NUMBER_PATTERNS
        self._entity_type = entities.phone_number.PhoneNumber()

    def recognize_all(self, text: str) -> list[entities.entity.NamedEntity]:
        recognized_entities = []
        lower_text = text.lower()

        for country, pattern in self._phone_number_patterns.items():
            # Create a regex to match phone numbers for a particular country
            regex = re.compile(pattern)
            matches = regex.finditer(lower_text)

            for match in matches:
                # Create a NamedEntity for each phone number match
                recognized_entities.append(entities.entity.NamedEntity(
                    name=match.group(), position=match.start(), entity_type=self._entity_type))

        return recognized_entities
