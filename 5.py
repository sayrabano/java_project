# # with help of f-string formatting string literals
# # name = "sayra"
# # adjective = "Green"
# # noun = "Tom"

# mad_libs = "{name} laughed at {adjective} {noun}."
# # print(mad_libs)
# # print(f"2+2 is{4+5}")
# name = ("enter name ")
# noun = ("Enter noun ")
# adjective = ("Enter adj ")

# print(mad_libs.format(name=name, adjective=adjective, noun=noun))
# # print(mad_libs)

class Teddy:
    quantity = 50
    def __init__(This,name,color):
       This.name = name
       This.color = color
q = Teddy("sayra","blue")
print(q.name)
print(q.color)