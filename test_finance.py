from finance import calculate_savings, discount_price


def test_calculate_savings():
    assert calculate_savings(5000, 3200) == 1800


def test_discount_price():
    assert discount_price(100, 20) == 80

def test_calculate_tax():
    from finance import calculate_tax
    assert calculate_tax(1000, 23) == 230   