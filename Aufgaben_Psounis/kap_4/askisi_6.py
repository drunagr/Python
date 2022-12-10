my_list = [1, 5, 3]
print(my_list)

my_list.insert(0, 9)
print(my_list)

list2 = my_list[:]

list3 = [16, 13]

my_list.extend(list3)

print(my_list)

last = my_list.pop(0)
print(my_list)
print(last)
my_list.sort()
print(my_list)
print(my_list[::-1])
my_list.sort(reverse=True)
print(my_list)

my_list.remove(1)
print(my_list)