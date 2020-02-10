import sqlite3
import csv
import os

dirname      = os.path.dirname(__file__)
filename     = os.path.join(dirname,'test.db')
filename_csv = os.path.join(dirname,'employee.csv')

conn    = sqlite3.connect(filename)
cur     = conn.cursor()
records = []

with open(filename_csv,'r') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        records.append(row)    
# print(records)
cur.executemany("INSERT INTO employees (employee_name,age,gender,country,city,role,salary) VALUES (?,?,?,?,?,?,?)", records)
conn.commit()
conn.close()