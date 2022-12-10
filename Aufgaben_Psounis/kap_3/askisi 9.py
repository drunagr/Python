ak_1 = int(input("zahl 1: "))
ak_2 = int(input("zahl 2: "))
ak_3 = int(input("zahl 3: "))

maximum = ak_1

if ak_2 > maximum:
    maximum = ak_2
if ak_3 > maximum:
    maximum = ak_3

print("the max is: ", maximum)