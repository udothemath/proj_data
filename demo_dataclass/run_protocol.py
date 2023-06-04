from typing_extensions import Protocol
from dataclasses import dataclass
from datetime import datetime

# ## ref: https://www.youtube.com/watch?v=yatgY4NpZXE


@dataclass
class Customer:
    name: str
    phone: str
    exp_year: int
    exp_month: int
    card_valid: bool = True


class CardInfo(Protocol):
    @property
    def card_number(self):
        ...

    @property
    def exp_year(self):
        ...

    @property
    def exp_month(self):
        ...


def validate_card(card: CardInfo):
    return datetime(card.exp_year, card.exp_month, 1) > datetime.now()


def main() -> None:
    mike = Customer(
        name="Mike",
        phone="1234",
        exp_year=2000,
        exp_month=2,
    )
    print("--- Start ___")
    print("Current time:", datetime.now())
    print(mike)
    mike.card_valid = validate_card(mike)
    print(f"Is the card valid? {mike.card_valid}")

    print("--- Done ---")


if __name__ == "__main__":
    main()
