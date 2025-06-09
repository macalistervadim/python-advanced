"""
В классе A реализован метод __iadd__, поэтому операция a += b изменяет объект a на месте (id объекта не меняется).
В классе B реализован только __add__, поэтому при b += a вызывается __add__, создаётся новый объект, и переменная b начинает ссылаться на него (id меняется).
Если у объекта не реализован __iadd__, Python использует __add__, и операция a += b эквивалентна a = a + b.
"""


class A:
    def __init__(self, value):
        self.value = value

    def __iadd__(self, other):
        self.value += other.value

        return self

    def __repr__(self):
        return f"A({self.value})"


class B:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return B(self.value + other.value)

    def __repr__(self):
        return f"B({self.value})"


a = A(10)
b = B(20)

print(id(a))
a += b
print(id(a))

print(id(b))
b += a
print(id(b))


a = (1, 2, 3)
