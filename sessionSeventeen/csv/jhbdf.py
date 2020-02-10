import csv
import os
import configparser as cf

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'people.csv')

csv.register_dialect('myDia', delimiter = ';', quoting = csv.QUOTE_NONE ,skipinitialspace = True)

""" with open(filename,'r') as file:
    reader = csv.reader(file, dialect = 'myDia')
    for row in reader:
        print(row) """

""" with open(filename,'w', newline = '') as file:
    writer = csv.writer(file)
    writer.writerow(['SN', 'Movie', 'Protagonist', 'Country'])
    writer.writerow(['2', 'Lord of the Rings', 'Frodo Baggins', 'Country One'])
    writer.writerow(['1', 'Harry Potter', 'Harry Potter', 'Country Two']) """

csv_rowlist = [['SN', 'Movie', 'Protagonist', 'Country'], ['2', 'Lord of the Rings', 'Frodo Baggins', 'Country One'], ['1', 'Harry Potter', 'Harry Potter', 'Country Two']]

""" with open(filename,'w', newline = '') as file:
    writer = csv.writer(file)
    writer.writerows(csv_rowlist) """

