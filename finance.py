def calculate_savings(income, expenses):
    return float(income - expenses)

def discount_price(price, discount_percent):
    return price - (price * discount_percent / 100)

def calculate_tax(amount, tax_percent):
    return amount * tax_percent / 100