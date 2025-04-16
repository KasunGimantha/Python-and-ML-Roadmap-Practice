# You’re handed some faulty code. Fix it using your understanding of scoping.

# secret_code = "XYZ123"

# def decode():
#     secret_code = "ABC999"

# decode()
# print(secret_code)  # Output:

# 🧩 Goal:
# Explain why it prints "XYZ123" instead of "ABC999", and modify it so that calling decode() updates the global variable.


secret_code = "XYZ123"


def decode():
    global secret_code  # fix
    secret_code = "ABC999"


decode()

print(secret_code)


# The reason for  "XYZ123"(A) printing instead of "AB999"(B) is A declared in a global scope while B declared inside  a function,but not declared it as a global variable so A act as defalut global variable
