# Convert this loop into a list comprehension:

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# squared_numbers = []
# for num in numbers:
#     if num % 2 == 0:
#         squared_numbers.append(num ** 2)

squared_numbers = [
    num**2 for num in numbers if num % 2 == 0]

print(squared_numbers)
