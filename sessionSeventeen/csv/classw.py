import csv
import os
import vehicle

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'showroom_stock.csv')
filename_bike = os.path.join(dirname, 'bikes.csv')
Bikes = []
Cars  = []

with open(filename,'r') as file:
    reader = csv.reader(file)
    for row in reader:
        if row[0] == 'Bike':
            Bikes.append(row, vehicle.color)

print(Bike)
