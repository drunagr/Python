i = 1

while i <= 5:
    print("Hello")
    i += 1


number = str(input("enter a number(0-9): "))


while number < 0 or number > 9:
    number = int(input("between 0 and 9 please: "))

print("you entered: "+ str(number))


