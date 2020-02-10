def tableListing(table_starting,table_ending,steps):
    for x in range(table_starting,table_ending+1):
        for y in range(1,steps+1):
            print(f'{x} x {y} = {x*y}')

table_starting = int(input('Enter the start value :'))
table_ending   = int(input('Enter the end value :'))
steps          = int(input('Enter the length of the table :'))

tableListing(table_starting,table_ending,steps)