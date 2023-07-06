# %%
# from __future__ import annotations
from typing import Dict
from typing import List
import random
import string
from dataclasses import dataclass, field, asdict, astuple
from person import Person
from contextlib import closing
from pathlib import Path
from pydantic import BaseModel


ROOT = Path().absolute()
print(ROOT)


def gen_file():
    with closing(open('hello.txt', 'w')) as f:
        f.write('Hello world')


def generate_id() -> str:
    return "".join(random.choices(string.ascii_uppercase, k=12))


class PersonInBaseModel(BaseModel):
    name: str
    address: str
    active: bool = True
    email: List[str] = []
    id: str = "the_id"


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


def main2() -> None:
    person2 = PersonInDataclass(name="Mick", address="456 Maplewood Rd")
    print(person2)
    person3 = PersonInDataclass(
        name="Marry", address="789 Cbestnut Ridge", email=["aaa@g.com"], id='credit')
    print("person3: ", person3)
    print("person3.__dict__: ", person3.__dict__)
    print(person3.__dict__['_search_string'])

    person4 = PersonInBaseModel(name="Joe", address="111 Maplewood Rd", email=[
                                "99999@g.com"], id='debit')
    print(person4)


class Indenter:
    def __init__(self):
        self.level = 0

    def __enter__(self):
        self.level += 1
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.level -= 1

    def print(self, text):
        print('    ' * self.level + text)


def test_indenter():
    with Indenter() as indent:
        indent.print("Hello")
        with indent:
            indent.print("Task1")
            indent.print("Task2")
            with indent:
                indent.print("Invest:2.1")
                indent.print("Invest:2.2")
        indent.print("Done")


the_dict = {
    'type': 'K'
}


@dataclass(frozen=False)
class PoiType():
    x: int = 1
    y: str = 'the_str'
    z: list = field(default_factory=list)
    zz: Dict[str, str] = field(default_factory=lambda: {'type': 'abc'})


def main_poi():
    a = PoiType(x=123, y='adam', z=[5, 6, 7])
    print(a)
    print(a.__dict__)
    print(asdict(a))
    print(astuple(a))


if __name__ == "__main__":
    # main2()
    # gen_file()
    # test_indenter()
    # print(ROOT)
    main_poi()
    print("Done")

# %%
