# def calculator(operation,a,b):
#     if operation=="add":
#         return a+b

#     elif operation == "subtract":
#         return a-b

#     elif operation == "multiply":
#         return a*b

#     elif operation == "divide":
#         return a/b
#     else:
#         return "Not sure about the answer"

# print(calculator("add",4,8))

# print(calculator("subtract",47,8))

# print(calculator("multiply",14,8))

# print(calculator("divide",4,28))

# print(calculator(",",4,8))


zip_code = "902910"
# check
if len (zip_code):
    check = "Valid"
else:
     check = "Invalid"

check = "Valid" if len(zip_code) ==5 else "Invalid"
print(check)

# print(len(zip_code))
# print(zip_code("check"))