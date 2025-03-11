myclass = {
    "class1": {"Name": "Sunil", "Age": 23},
    "class2": {"Name": "Amal", "Age": 24},
    "class3": {"Name": "Kamal", "Age": 20}
}

for class_key, details in myclass.items():
    print(f"Class: {class_key}")
    for key, value in details.items():
        print(f"{key}:{value}")


print("\nFixed Dictionary:", myclass)  # Now all keys are consistent
