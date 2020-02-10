import csv
import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'people.csv')

with open(filename,'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)
        print(dict(row)['Name'])