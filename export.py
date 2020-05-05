import csv
import cx_Oracle


try:
 connection = cx_Oracle.connect("orcl/SYS:admin@localhost:1521/mydb")
except cx_Oracle.DatabaseError as exception:
    print('Not working database%s\n', database)
    print(exception)
    exit(1)
    
    
cur = connection.cursor()

tabl = ['Chocolate', 'Company', 'Bean']
for table in tabl:
    with open(table + '.csv', 'w', newline = '') as file:
        cur.execute('SELECT * FROM ' + table)
        rows = cur.fetchone()
        wrCSV = csv.writer(file, delimiter=',')
        while rows:
            wCSV.writerow(rows)
            rows = cur.fetchone()

cur.close()
connection.close()
