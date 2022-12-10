active = True

while active:
    user_input = input("type string or quit: ")

    if user_input == "quit":
        print("bye bye")
        active = False
    else:
        print("why " + user_input + "?")