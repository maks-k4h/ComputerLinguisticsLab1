import sys

from modules.recognizer import NamedEntityRecognizer


def main() -> None:
    text = sys.stdin.buffer.read().decode()
    recognizer = NamedEntityRecognizer()
    named_entities = recognizer.recognize_all(text)
    for named_entity in named_entities:
        print(f'{named_entity.entity_type.type_name} : {named_entity.name} : pos {named_entity.position}')


if __name__ == '__main__':
    main()
