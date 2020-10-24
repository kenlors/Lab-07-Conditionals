question = input("What kind of Operation would you want to do?")
if question == "mul":
    print(type(mul))
    mul = input(" " * " ")
    print(" The result is" + str(mul))
if question == "div":
    print(type(div))
    div = input(" " / " ")
    print("The result is" + str(div))
if question == "mod":
    print(type(mod))
    mod = input (" " % " ")
    print(" The result is " + str(mod))
else:
    print("Invalid Operation")
