N = 4

subsets = set()
subsets.add(frozenset())

for i in range(1, N+1):
    new_subsets = set()
    for subset in subsets:
        non_fz = set(subset)
        non_fz.add(i)
        fz = frozenset(non_fz)
        new_subsets.add(fz)
    subsets.update(new_subsets)

print(subsets)
