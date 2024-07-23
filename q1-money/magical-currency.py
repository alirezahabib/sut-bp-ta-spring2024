rates = {
    "IRT": 1,
    "USD": 59700,
    "EUR": 64550,
    "GBP": 75800,
    "CHF": 66450,
    "CAD": 43350,
    "TRY": 1845
}


class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def __add__(self, other):
        return Money(self.amount + other.amount * rates[other.currency] / rates[self.currency], self.currency)

    def __sub__(self, other):
        return Money(self.amount - other.amount * rates[other.currency] / rates[self.currency], self.currency)

    def __mul__(self, other):
        return Money(self.amount * other, self.currency)

    def __truediv__(self, other):
        if isinstance(other, Money):
            return self.amount * rates[self.currency] / (other.amount * rates[other.currency])
        return Money(self.amount / other, self.currency)

    def __floordiv__(self, other):
        if isinstance(other, Money):
            return self.amount * rates[self.currency] // (other.amount * rates[other.currency])
        return Money(self.amount // other, self.currency)

    def __str__(self):
        return f"{self.amount} {self.currency}"

    def __repr__(self):
        return f"{self.amount} {self.currency}"

    def __lt__(self, other):
        return self.amount * rates[self.currency] < other.amount * rates[other.currency]

    def __le__(self, other):
        return self.amount * rates[self.currency] <= other.amount * rates[other.currency]

    def __gt__(self, other):
        return self.amount * rates[self.currency] > other.amount * rates[other.currency]

    def __ge__(self, other):
        return self.amount * rates[self.currency] >= other.amount * rates[other.currency]

    def convert(self, currency):
        return Money(self.amount * rates[self.currency] / rates[currency], currency)


for _ in range(int(input())):
    print(eval(input()))
