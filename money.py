class Money:

    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency
        self.usd = 1
        self.eur = .9
        self.jpy = 110.65
        self.btc = .0019

    @property
    def currency_type(self):
        if self.usd:
            return self.amount * self.usd
        elif self.eur:
            return self.amount * self.eur
        elif self.jpy:
            return self.amount * self.jpy
        else:
            return self.amount * self.btc

    def __add__(self, other):
        return (self.currency_type * self.amount) + (other.currency_type * other.amount)

    def __mul__(self, other):
        return Money(self, other)

    def __lt__(self, other):
        return self.currency_type > other.currency_type


currency1 = Money(100.50, "usd")
currency2 = Money(200.50, "eur")
print(currency1 < currency2)
print(currency1 + currency2)