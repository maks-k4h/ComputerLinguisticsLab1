from . import recognizers, entities


class NamedEntityRecognizer(recognizers.abstract.AbstractRecognizer):
    def __init__(self) -> None:
        self._cities_recognizer = recognizers.cities.CityRecognizer()
        self._countries_recognizer = recognizers.countries.CountryRecognizer()
        self._geographical_recognizer = recognizers.geographical.GeographicalRecognizer()
        self._companies_recognizer = recognizers.companies.CompanyRecognizer()
        self._phone_number_recognizer = recognizers.phone_numbers.PhoneNumberRecognizer()
        self._email_recognizer = recognizers.emails.EmailRecognizer()

    def recognize_all(self, text: str) -> list[entities.entity.NamedEntity]:
        res = []
        res += self._cities_recognizer.recognize_all(text)
        res += self._countries_recognizer.recognize_all(text)
        res += self._geographical_recognizer.recognize_all(text)
        res += self._companies_recognizer.recognize_all(text)
        res += self._phone_number_recognizer.recognize_all(text)
        res += self._email_recognizer.recognize_all(text)

        return res
