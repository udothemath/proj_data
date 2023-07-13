from functools import partial
from dataclasses import dataclass
import timeit
from typing import Union


def multiply(a, b):
    return a * b


def use_partial(x, y=5):
    f = partial(multiply, y)
    result = f(x)
    print(result)

class Person:
    def __init__(self, name: str, age: int, address: str):
        self.name = name
        self.age = age
        self.address = address

class PersonSlots:
    __slots__ = "name", "age", "address"
    def __init__(self, name: str, age: int, address: str):
        self.name = name
        self.age = age
        self.address = address

def get_set_delete(person: Union[Person, PersonSlots]):
    person.address = "123 MapleWood Rd"
    _ = person.address
    del person.address
    
if __name__ == "__main__":
    # print(multiply(a=3, b=5))
    # use_partial(2)
    # use_partial(10)
    person = Person("john", 33, "main street")
    person_slots = PersonSlots("john", 33, "main street")

    no_slots = min(timeit.repeat(partial(get_set_delete, person), number=100000))

    slots = min(timeit.repeat(partial(get_set_delete, person_slots), number=100000))

    print(f"no_slots: {no_slots:.4f}")
    print(f"slots: {slots:.4f}")
    # print(a.name, a.age, a.address)
    # get_set_delete(a)

# Ref
# https://www.pythontutorial.net/python-basics/python-partial-functions/
# https://www.geeksforgeeks.org/partial-functions-python/
