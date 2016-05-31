class Money:

    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency
        self.usd = 'usd'
        self.eur = 'eur'
        self.jpy = 'jpy'
        self.btc = 'btc'

    @property
    def currency_type(self):
        if self.currency.lower() == self.usd:
            return self.amount
        elif self.currency.lower() == self.eur:
            return self.amount * .9
        elif self.currency.lower() == self.jpy:
            return self.amount * 110.65
        elif self.currency.lower() == self.btc:
            return self.amount * .0019
        else:
            return "Invalid Input"

    def __str__(self):
        return "{}".format(self.currency_type)

    def __eq__(self, other):
        return self.currency_type == other.currency_type

    def __ne__(self, other):
        return self.currency_type != other.currency_type

    def __add__(self, other):
        return Money(self.currency_type + other.currency_type, "usd")

    def __mul__(self, other):
        return self.currency_type * other.currency_type

    def __sub__(self, other):
        return self.currency_type - other.currency_type

    def __lt__(self, other):
        return self.currency_type < other.currency_type

    def __le__(self, other):
        return self.currency_type <= other.currency_type

    def __gt__(self, other):
        return self.currency_type > other.currency_type

    def __ge__(self, other):
        return self.currency_type >= other.currency_type


usd = Money(100.50, "USD")
eur = Money(100.50, "eur")
jpy = Money(100.50, "JPY")
btc = Money(100.50, "btc")
addition = usd + eur
multiplication = usd * btc
subtraction = jpy - eur

print("USD to EUR: $", eur)
print("USD to JPY: $", jpy)
print("USD to BTC: $", btc)

print("USD == EUR: ", usd == eur)
print("BTC != EUR: ", btc != eur)
print("JPY <= EUR: ", jpy <= eur)
print("USD < EUR: ", usd < eur)
print("USD >= EUR: ", usd >= eur)
print("USD > EUR: ", usd > eur)
print("USD + EUR: ", addition)
print("JPY - EUR: ", subtraction)
print("USD * BTC: ", multiplication)
print("BTC + EUR: ", btc + eur)

print("String addition", (Money(100.00, "usd") + Money(56.32, "eur") + Money(1.2, "btc") + Money(8, "jpy")))
