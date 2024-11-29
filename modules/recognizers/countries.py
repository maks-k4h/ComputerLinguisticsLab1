from .abstract import AbstractRecognizer
from .. import entities

from . import data


class CountryRecognizer(AbstractRecognizer):
    def __init__(self) -> None:
        self._country_list = data.countries.ALL_COUNTRIES
        self._entity_type = entities.country.Country()

    def recognize_all(self, text: str) -> list[entities.entity.NamedEntity]:
        recognized_entities = []
        lower_text = text.lower()

        for country in self._country_list:
            country_lower = country.lower()
            start = 0

            while True:
                start = lower_text.find(country_lower, start)
                if start == -1:
                    break

                # Create a NamedEntity for each occurrence
                recognized_entities.append(entities.entity.NamedEntity(
                    name=country, position=start, entity_type=self._entity_type))
                start += len(country_lower)  # Move start to avoid overlapping matches

        return recognized_entities
