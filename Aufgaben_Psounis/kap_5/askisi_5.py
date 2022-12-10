cities = ["athens", "rodos", "kalamata", "kos", "sparta"]

results = []
for index in range(0, len(cities), 2):
    results.append(cities[index])
print(results)