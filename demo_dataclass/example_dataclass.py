import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    return "".join(random.choices(string.ascii_uppercase, k=12))


class Person:
    def __init__(self, name: str, address: str):
        self.name = name
        self.address = address

    def __str__(self):
        return f"{self.name}, {self.address}"


@dataclass(frozen=False)
class PersonInDataclass:
    name: str
    address: str
    active: bool = True
    email: list = field(default_factory=list)
    id: str = field(default_factory=generate_id)
    _search_string: str = field(init=False, repr=False)  # for post_init

    def __post_init__(self) -> None:
        self._search_string = f"Search: {self.name}, {self.address}"


def main1() -> Person:
    person1 = Person(name="John", address="123 Main St")
    print(person1)


def main2() -> PersonInDataclass:
    person2 = PersonInDataclass(name="Mick", address="456 Maplewood Rd")
    print(person2)
    person3 = PersonInDataclass(
        name="Marry", address="789 Cbestnut Ridge", id='credit')
    print(person3)
    print(person3.__dict__)
    print(person3.__dict__['_search_string'])


if __name__ == "__main__":
    main2()
