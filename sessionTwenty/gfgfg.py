import sqlite3
import os

dirname  = os.path.dirname(__file__)
filename = os.path.join(dirname,'test.db')

records = ((111,'NameOne',32,'California',255555),(112,'NameOne',32,'California',255555),(113,'NameOne',32,'California',255555),(114,'NameOne',32,'California',255555),(115,'NameOne',32,'California',255555),(116,'NameOne',32,'California',255555),(117,'NameOne',32,'California',255555),(118,'NameOne',32,'California',255555),(119,'NameOne',32,'California',255555),(120,'NameOne',32,'California',255555),(121,'NameOne',32,'California',255555))

conn = sqlite3.connect(filename)
cur = conn.cursor()

cur.executemany("INSERT INTO COMPANY VALUES (?,?,?,?,?)", records)

""" cur.execute("DELETE FROM COMPANY WHERE ID=''")"""

""" cur.execute("SELECT * FROM COMPANY")
print(cur.fetchone())
print('--------------------------------------')
print(cur.fetchmany(10))
print('--------------------------------------')
print(cur.fetchall()) """

"""for row in cur:
    print("ID = ",row[0])
    print("NAME = ",row[1])
    print("AGE = ",row[2])
    print("ADDRESS = ",row[3])
    print("SALARY = ",row[4],"\n") """
""" for record in records:
    cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (?, ?, ?, ?, ?) ", (record[0],record[1],record[2],record[3],record[4])) """

"""cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (1,'Paul',?,?,20000.00), (32,'Texas')")

conn.commit()
print(conn.total_changes)
 """
 
conn.commit()
conn.close()