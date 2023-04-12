
import random
data = []
for i in range(3):
    name = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=5))
    age = random.randint(18, 60)
    data.append({'name': name, 'age': age})

# Sort data by age
data.sort(key=lambda x: x['age'])

# Print sorted data
for d in data:
    print(f"Name: {d['name']}, Age: {d['age']}")
