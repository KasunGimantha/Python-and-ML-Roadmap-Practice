# create a dictionary

my_dict = {23: 'Kamal', 25: 'Amal', 30: 'Nimal', 20: 'Sunil'}

# create function


def reverse_dict(old_dict, new_dict={}):
    # swapping key and value
    new_dict = dict([(value, key) for key, value in old_dict.items()])
    return new_dict


new_dict = reverse_dict(my_dict)  # store old dictionary
print(my_dict) #old dictionary
print(new_dict) #new dictionary

