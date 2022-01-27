
def hi(name):
    if name == "Valini":
        print("Good Day!" + name)
    elif name == "Ruby":
        print ("Hi Ruby!, Long time no see")
    else:
        print("Unknown!")
        g = str(input("Re-enter your name:"))
        print("Good Day" + g )
u = str(input("Enter name: "))
hi(u)


