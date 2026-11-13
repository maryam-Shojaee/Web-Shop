class Product:
    def __init__(self, sku, name, price):
        self.sku = sku
        self.name = name
        self.price = price

def apply_discount(price, percent):
    return price * (100 - percent) / 100

def add_tax(price, rate=0.2):
    return price * (1 + rate)
