# MRO means method Resolution Order
# youtube: https://www.youtube.com/watch?v=X1PQ7zzltz4&t=1s
# github: https://github.com/mCodingLLC/VideosSampleCode/blob/master/videos/093_super_in_python/multiple_inheritance.py

class ValidatedSet(set):
    def __init__(self, *args, validators=None, **kwargs):
        self.validators = list(validators) if validators is not None else []
        if args:
            (elements,) = args
            self.validate_many(elements)
        super().__init__(*args, **kwargs)

    def validate_one(self, element):
        for f in self.validators:
            if not f(element):
                raise ValueError(
                    f"invalid element: {element}. Rule: {f.__name__}")

    def validate_many(self, elements):
        if not self.validators:
            return
        for elem in elements:
            self.validate_one(elem)

    def add_check(self, element):
        self.validate_one(element)
        super().add(element)


def is_int(x):
    return isinstance(x, int)


def is_smaller_than_10(x):
    return x < 10


def validated_set_example():
    print(" --- Validate in progress --- ")
    ints = ValidatedSet([1, 2, 3], validators=[is_int, is_smaller_than_10])
    ints.add_check(9)
    # ints.add_check(999)
    print(ints)
    print(" --- Done --- ")


if __name__ == "__main__":
    validated_set_example()
