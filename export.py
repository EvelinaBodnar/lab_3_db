import csv
import cx_Oracle
connection = cx_Oracle.connect("orcl/SYS:admin@localhost:1521/mydb")
cur = connection.cursor()

tables = ['Chocolate', 'Company', 'Bean']
for table in tables:
    with open(table + '.csv', 'w', newline = '') as csvfile:
        cur.execute('SELECT * FROM ' + table)
        rows = cursor.fetchone()
        writeCSV = csv.writer(csvfile, delimiter=',')
        while rows:
            writeCSV.writerow(rows)
            rows = cur.fetchone()
cur.close()
connection.close()
