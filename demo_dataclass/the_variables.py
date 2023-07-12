# %%
class TheVariables:
    def __init__(self, larger_than_100, negative_value):
        self.larger_than_100 = larger_than_100
        self.negative_value = negative_value

    @property
    def check_larger_than_100(self):
        return self.larger_than_100

    def check_input_value(self, input_value: int):
        if input_value < 100:
            raise ValueError


def input_abc():
    print("start to input value")
    a = int(input("a= "))
    b = int(input("b= "))
    c = int(input("c= "))
    print(f"a={a}, b={b}, c={c}")
    print("end of input value")


# vars = TheVariables(1000, -123)
# vars.check_input_value(1)

# input_abc()

# %%
