d_array = []

rows = int(input('give number of rows: '))
cols = int(input('give number of columns: '))

for i in range(rows):
    d_array.append([])
    for j in range(cols):
        elem = int(input('give ' + str(i) + ',' + str(j) + ' element: ' ))
        d_array[i].append(elem)

print(d_array)