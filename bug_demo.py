def calculate_total(price, quantity):
    total = price * quantity
    return total


def apply_discount(total, percent):
    discount = total * percent / 100
    return total - discount


price = 50000
quantity = 3
total = calculate_total(price, quantity)
final = apply_discount(total, 10)
print("Total:", total)
print("After discount:", final)