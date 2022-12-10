def euclid(a,b):
    if a == b:
        return a
    elif a < b:
        return euclid(a, b-a)
    else:
        return euclid(a-b, b)

number1 = int(input("give first number for GGT(grösste gemeinsame Teiler): "))
number2 = int(input("give second number for GGT(grösste gemeinsame Teiler): "))

print(f"GGT von {number1} und {number2} ist: {euclid(number1, number2)}")