import re
from .abstract import AbstractRecognizer
from .. import entities
from . import data


class EmailRecognizer(AbstractRecognizer):
    def __init__(self) -> None:
        # Email recognizer doesn't require a predefined list like companies or phone numbers.
        # We will use a regex pattern to detect emails.
        self._entity_type = entities.email.Email()

    def recognize_all(self, text: str) -> list[entities.entity.NamedEntity]:
        recognized_entities = []
        lower_text = text.lower()

        # Define a simple regex pattern for recognizing email addresses
        email_regex = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        matches = re.finditer(email_regex, lower_text)

        for match in matches:
            # Create a NamedEntity for each email address match
            recognized_entities.append(entities.entity.NamedEntity(
                name=match.group(), position=match.start(), entity_type=self._entity_type))

        return recognized_entities
