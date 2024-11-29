ALL_PHONE_NUMBER_PATTERNS = {
    # US Phone Numbers (e.g., (555) 123-4567 or 555-123-4567)
    "US": r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}",

    # UK Phone Numbers (e.g., +44 20 7946 0958 or 020 7946 0958)
    "UK": r"(\+44\s?(\d{4}|\d{3})\s?\d{4}|\(?\d{2,5}\)?\s?\d{3,4}\s?\d{3,4})",

    # Indian Phone Numbers (e.g., +91-9876543210 or 9876543210)
    "IN": r"\(?\+?91\)?[-.\s]?\d{10}",

    # Canadian Phone Numbers (e.g., (416) 555-1234 or 416-555-1234)
    "CA": r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}",

    # Australian Phone Numbers (e.g., +61 2 9876 5432 or 02 9876 5432)
    "AU": r"\(?\+?61\)?[-.\s]?\d{1,2}[-.\s]?\d{4}[-.\s]?\d{4}",

    # German Phone Numbers (e.g., +49 170 1234567 or 0170 1234567)
    "DE": r"\(?\+?49\)?[-.\s]?\d{1,5}[-.\s]?\d{1,8}",

    # Brazilian Phone Numbers (e.g., +55 11 98765-4321 or (11) 98765-4321)
    "BR": r"\(?\+?55\)?[-.\s]?\d{2}[-.\s]?\d{5}[-.\s]?\d{4}",

    # French Phone Numbers (e.g., +33 1 70 18 34 56 or 01 70 18 34 56)
    "FR": r"\(?\+?33\)?[-.\s]?\d{1}[-.\s]?\d{2}[-.\s]?\d{2}[-.\s]?\d{2}[-.\s]?\d{2}",

    # Japanese Phone Numbers (e.g., +81 90-1234-5678 or 090-1234-5678)
    "JP": r"\(?\+?81\)?[-.\s]?\d{1,4}[-.\s]?\d{1,4}[-.\s]?\d{4}",

    # South African Phone Numbers (e.g., +27 11 123 4567 or 011 123 4567)
    "ZA": r"\(?\+?27\)?[-.\s]?\d{1,2}[-.\s]?\d{3}[-.\s]?\d{4}",
}
