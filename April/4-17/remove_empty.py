# Write a single line list comprehension that:

# Removes empty strings

# Converts messages to uppercase

messages = ["Encrypt this", "", "Send help", "", "Urgent: reply", ""]


print([x.upper() for x in messages if x.strip()])