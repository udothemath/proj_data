import pytest
from person import Person


class TypeError(Exception):
    pass


def test_person_str():
    p = Person("Alice", "123 Main St")
    assert str(p) == "Alice, 123 Main St"


def test_person_name_type():
    with pytest.raises(TypeError) as e_info:
        p = Person(1234, "456 Broad St")
        print(e_info)
        raise TypeError('Name must be string')


def test_person_address_type():
    with pytest.raises(TypeError):
        p = Person("Bob", 1234)
        raise TypeError('Address must be string')


def test_person_name_property():
    p = Person("Charlie", "789 Market St")
    assert p.name == "Charlie"


def test_person_address_property():
    p = Person("Dave", "987 Oak Ave")
    assert p.address == "987 Oak Ave"
