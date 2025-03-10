# $declaring dictionary

myclass = {
    "class1": {"name": "Sunil", "Age": 23}, "class2": {"Name": "Amal", "Age": 24}, "class3": {"Name": "Kamal", "Age": 20}
}
# declare dynamic dictionary
dynamic_dict = {}

for key, value in myclass.items():
    if key in dynamic_dict:
        dynamic_dict[key] += value
    else:
        dynamic_dict[key] = value

print(dynamic_dict)
