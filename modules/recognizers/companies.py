from .abstract import AbstractRecognizer
from .. import entities

from . import data


class CompanyRecognizer(AbstractRecognizer):
    def __init__(self) -> None:
        self._company_list = data.companies.ALL_COMPANIES
        self._entity_type = entities.company.Company()

    def recognize_all(self, text: str) -> list[entities.entity.NamedEntity]:
        recognized_entities = []
        lower_text = text.lower()

        for city in self._company_list:
            city_lower = city.lower()
            start = 0

            while True:
                start = lower_text.find(city_lower, start)
                if start == -1:
                    break

                # Create a NamedEntity for each occurrence
                recognized_entities.append(entities.entity.NamedEntity(
                    name=city, position=start, entity_type=self._entity_type))
                start += len(city_lower)  # Move start to avoid overlapping matches

        return recognized_entities
