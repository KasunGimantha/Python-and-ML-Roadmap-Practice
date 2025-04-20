def calculate_discount(price, discount_percent):

    if isinstance(price, (int, float)) and isinstance(discount_percent, (int, float)):
        if price >= 0:
            if 0 <= discount_percent and discount_percent <= 100:
                discount = price*(1-discount_percent/100)
                return round(discount, 2)
            else:
                raise ValueError("Discount percent must be between 0 and 100")
        else:
            raise ValueError("price can't be negative")
    else:
        raise ValueError("Enter valid type")


# print(calculate_discount("free", 20))
# print(calculate_discount(100, "ten"))
# print(calculate_discount(-10, 20))
# print(calculate_discount(100, 130))
print(calculate_discount(100, 20))
