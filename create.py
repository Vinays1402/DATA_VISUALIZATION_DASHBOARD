import csv

data = [
    ['Category', 'Value'],
    ['A', 10],
    ['B', 20],
    ['C', 15],
    ['D', 25],
    ['E', 30]
]

filename = 'data.csv'

with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print(f'{filename} created successfully.')
