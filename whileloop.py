# count = 2

# while count<=15:
#     print(count)
#     count+=3
# print(count)
invalid_number = True
while invalid_number:
    user_value = int(input("Enter a number above 10: "))
    if user_value>10:
        print("Thanks,thats wrks! is a great choice")
        invalid_number = False

    else:
        print("ok")
print("stop")        