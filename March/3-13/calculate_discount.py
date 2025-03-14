class MaxMinPercentageError(Exception):  # custom  exception
    "Raised when discount is below 0% and above 100%"
    pass


final_price = 0  # declaring global variable


def calculate_discount(price, discount_percent):
    global final_price  # modify global variable inside function
    try:

        if discount_percent > 100 or discount_percent < 0:
            raise MaxMinPercentageError("Invalid discount percentage")
        discount = price*(discount_percent/100)
        final_price = price - discount
        return final_price
    except MaxMinPercentageError as e:
        print(f"Exception occurred: {e}")
        return None


print(calculate_discount(100, 10))
