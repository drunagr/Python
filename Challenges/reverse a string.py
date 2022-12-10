def reverse_string(text):
    
    if len(text) <= 1:
        return text

    first_char = text[0]
    remaining = text[1:]

    return reverse_string(remaining) + first_char



while True:
    print()
    my_text = input("give a string to reverse: ")
    print()
    print(reverse_string(my_text))
    print()
    antwort = str.upper(input("Do you have another Text? (yes/No): "))
    

    if antwort == "NO":
        print("OK, BYE!!!")
        print()
        break