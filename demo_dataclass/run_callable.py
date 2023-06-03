from typing import Callable
from typing_extensions import Protocol
from typing import List
from functools import partial


def handle_payment(amount: int) -> None:
    print(f"Charge: ${amount} ")


PRICES = {
    "burger": 15,
    "drink": 5,
    "salad": 10
}


class StripePaymentHandler:
    def handle_payment(self, amount: int) -> None:
        print(f"Charge: ${amount} using Stripe")


class PaymentHandler(Protocol):
    def handle_payment(self, amount: int) -> None:
        ...


def handle_payment_stripe_as_func(amount: int) -> None:
    print(f"Charge: ${amount} using Stripe")


HandlePaymentFn = Callable[[int], None]


def order_food_approach1(items: List[str], payment_handler: PaymentHandler) -> None:
    print("-- approach 1 ---")
    print(f"your orfer: {items}")
    total = sum(PRICES[item] for item in items)
    print(f"order total: {total}")
    payment_handler.handle_payment(total)
    print("--- order completed --- ")


def order_food_approach2(items: List[str], payment_handler: HandlePaymentFn) -> None:
    print("-- approach 2 ---")
    print(f"your orfer: {items}")
    total = sum(PRICES[item] for item in items)
    print(f"order total: {total}")
    payment_handler(total)
    print("--- order completed ---")


order_using_strip = partial(
    order_food_approach1, payment_handler=StripePaymentHandler())


def main() -> None:
    print("Hello world")
    alices_order = ['burger', 'drink']
    order_food_approach1(alices_order, StripePaymentHandler())

    mikes_order = ['burger', 'burger', 'drink', 'salad']
    order_food_approach2(mikes_order, handle_payment_stripe_as_func)

    emilys_order = ['drink', 'salad']
    order_using_strip(emilys_order)


if __name__ == "__main__":
    main()
