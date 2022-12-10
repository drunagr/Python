ak_1 = int(input("zahl 1: "))
ak_2 = int(input("zahl 2: "))
ak_3 = int(input("zahl 3: "))

maximum = 0

if ak_1 < ak_2:
    maximum = ak_2
else:
    maximum = ak_1
if maximum >= ak_3:
    pass
else:
    maximum = ak_3

print("the max is: ", maximum)