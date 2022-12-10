from itertools import combinations


kom = []
A = [num for num in range(1,51)]
# print(len(A))
temp = combinations(A, 5)
for i in list(temp):
	kom.append(i)
peninta = len(kom)
# print(kom[:70])
print(peninta)


komp = []
A = [num for num in range(1,13)]
# print(len(A))
temp1 = combinations(A, 2)
for i in list(temp1):
	komp.append(i)
dodeka = len(komp)
print(dodeka)

print(peninta * dodeka, "\n")



def mutations(n, k):
    if n == k:
        return 1
    elif k == 1:
        return n
    else:
        return mutations(n-1, k-1) + mutations(n-1, k)

print(mutations(50, 5) * mutations(12, 2))