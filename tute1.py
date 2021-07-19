# a = int(input("Enter first number:" ))
# b = int(input("Enter second number:" ))
# sum = a+b
# print ("The sum of two no. is : ",a+b)
# ac = float(input("temperature"))
# celsius_temp = (ac-32)*(5/9)
# print("tem is: ",celsius_temp)

def out_text():
    print("hi")
    print("bye")

# out_text()
browser = "Google chrome"
print(browser.find("o"))
print(browser.find("g"))
print(browser.find("o",2))
print(browser.find("gle"))
print(browser.find("z"))
# index method
print(browser.index("G"))
# print(browser.index("z"))
print(browser.index("me"))
print(browser.startswith("g"))
print(browser.startswith("Goo"))
print(browser.endswith("rome"))
print(browser.endswith("e"))
print(browser.count("o"))
print(browser.count("me"))
w = "queueing"
print(w.count("ue"))
print(w.count("ing"))
print(w.count("u"))
print(w.count("u") + w.count("e"))
print(w.count("e"))